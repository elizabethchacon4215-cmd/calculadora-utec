import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import symbols, simplify, solve, Lambda

st.set_page_config(page_title="Calculadora UTEC", layout="wide")
st.title("🧮 Calculadora de Funciones - Matemática I")

# Requerimiento: Ingreso de la función
input_func = st.sidebar.text_input("Escribe tu función f(x):", "x**2 - 4*x + 3")

if input_func:
    try:
        x = symbols('x')
        f_expr = simplify(input_func)
        
        # Requerimiento: Gráfico interactivo con ejes y escala
        st.subheader("1. Gráfico de la Función")
        x_vals = np.linspace(-10, 10, 400)
        f_num = [float(f_expr.subs(x, val)) for val in x_vals]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_vals, y=f_num, name="f(x)"))
        fig.update_layout(xaxis_title="Eje X", yaxis_title="Eje Y")
        st.plotly_chart(fig)

        # Requerimiento: Puntos de corte
        st.subheader("2. Puntos de Corte")
        cortes_x = solve(f_expr, x)
        corte_y = f_expr.subs(x, 0)
        st.write(f"*Cortes en X (Raíces):* {cortes_x}")
        st.write(f"*Corte en Y:* (0, {corte_y})")

    except:
        st.error("Error en el formato. Usa x**2 para potencias.")
