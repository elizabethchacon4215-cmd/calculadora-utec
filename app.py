import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, simplify, solve, periodicity, is_increasing, is_decreasing
import pandas as pd
import re

# Configuración de página con estilo
st.set_page_config(page_title="Analizador Pro UTEC", layout="wide", initial_sidebar_state="expanded")

# Estilo personalizado con CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stTitle { color: #1E3A8A; font-family: 'Helvetica'; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Analizador de Funciones Inteligente - Ciclo 01-2026")
st.markdown("---")

def limpiar_entrada(texto):
    texto = texto.lower().replace(" ", "")
    texto = re.sub(r'x(\d+)', r'x**\1', texto)
    texto = re.sub(r'(\d+)x', r'\1*x', texto)
    return texto

# Sidebar mejorada
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png", width=50)
st.sidebar.header("⚙️ Panel de Control")
raw_input = st.sidebar.text_input("Ingresa tu función:", "x2 - 4x + 3")
rango_x = st.sidebar.slider("Rango de visualización (Eje X):", -50, 50, (-10, 10))

if raw_input:
    try:
        input_func = limpiar_entrada(raw_input)
        x = symbols('x')
        f_expr = simplify(input_func)
        
        # Layout de columnas
        col_graf, col_data = st.columns([2, 1])

        with col_graf:
            st.subheader("📊 Gráfica Interactiva Profesional")
            x_vals = np.linspace(rango_x[0], rango_x[1], 500)
            # Manejo de errores en evaluación numérica para asíntotas
            f_num = []
            for val in x_vals:
                try:
                    res = float(f_expr.subs(x, val))
                    f_num.append(res)
                except:
                    f_num.append(None)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=x_vals, y=f_num, name="f(x)", line=dict(color='#2563EB', width=4)))
            fig.update_layout(
                template="plotly_white",
                xaxis=dict(title="Eje X (Dominio)", showgrid=True, zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                yaxis=dict(title="Eje Y (Rango)", showgrid=True, zeroline=True, zerolinewidth=2, zerolinecolor='black'),
                margin=dict(l=20, r=20, t=20, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)

        with col_data:
            st.subheader("🔍 Análisis Matemático")
            
            # Cortes
            cortes_x = solve(f_expr, x)
            corte_y = f_expr.subs(x, 0)
            
            st.info(f"*Función Simplificada:* ${f_expr}$")
            
            st.markdown("---")
            st.write("*📍 Puntos Críticos:*")
            st.success(f"Cortes en X: {cortes_x}")
            st.success(f"Corte en Y: {corte_y}")
            
            # Tabla de valores rápida
            st.markdown("---")
            st.write("*📋 Tabla de Muestreo:*")
            puntos_tabla = np.linspace(rango_x[0], rango_x[1], 10)
            df = pd.DataFrame({
                'x': puntos_tabla,
                'f(x)': [float(f_expr.subs(x, p)) for p in puntos_tabla]
            })
            st.dataframe(df.style.format("{:.2f}"), use_container_width=True)
    except Exception as e:
        st.error(f"Error en la expresión. Revisa que esté bien escrita.")

st.sidebar.markdown("---")
st.sidebar.caption("Proyecto UTEC - Matemática I")
