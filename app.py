import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, simplify, solve
import re

st.set_page_config(page_title="Calculadora UTEC", layout="wide")
st.title("🧮 Calculadora de Funciones - Matemática I")

# El "Traductor" para no usar asteriscos
def limpiar_entrada(texto):
    texto = texto.lower().replace(" ", "")
    # Traduce x2 a x*2, x3 a x*3, etc.
    texto = re.sub(r'x(\d+)', r'x**\1', texto)
    # Traduce 2x a 2*x, 5x a 5*x, etc.
    texto = re.sub(r'(\d+)x', r'\1*x', texto)
    return texto

st.sidebar.header("Entrada de Datos")
raw_input = st.sidebar.text_input("Escribe tu función (ej: x2 - 4x + 3):", "x2 - 4x + 3")

if raw_input:
    try:
        # Aplicamos la limpieza automática
        input_func = limpiar_entrada(raw_input)
        x = symbols('x')
        f_expr = simplify(input_func)
        
        st.subheader(f"Análisis de: f(x) = {raw_input}")
        
        # Gráfico
        x_vals = np.linspace(-10, 10, 400)
        f_num = [float(f_expr.subs(x, val)) for val in x_vals]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=f_num, name="f(x)", line=dict(color='#0078D4', width=3)))
        fig.update_layout(xaxis_title="Eje X", yaxis_title="Eje Y")
        st.plotly_chart(fig)

        # Cortes
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 📍 Puntos de Corte")
            st.write(f"*En X:* {solve(f_expr, x)}")
            st.write(f"*En Y:* (0, {f_expr.subs(x, 0)})")
        with c2:
            st.markdown("### 📝 Info")
            st.write("Análisis generado automáticamente para el Ciclo 01-2026.")

    except:
        st.error("Revisa la escritura. Ejemplo: 3x2 + 2x - 5")
