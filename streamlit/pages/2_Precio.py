import streamlit as st

st.set_page_config(layout="wide")

import sys
sys.path.append("../")
import src.soporte as sp

st.write("<h1 style='text-align: center;'>Precio Energético</h1>", unsafe_allow_html=True)
"---"
st.markdown("###### Los datos son referentes al precio energético nacional, influyen pero no son iguales al precio doméstico.")
st.plotly_chart(sp.px_precio_historico(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
st.markdown("- En primavera de 2021 hay un aumento por la escasez de gas, seguido por el comflicto de Ukrania-Rusia en primavera del 2022.")


st.write("<h2 style='text-align: center;'>Análisis Anual</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### En el análisis anual, el precio energético vienen representados de forma horaria.")
col1, relleno = st.columns([1,4])
with col1:
    año = st.selectbox(
        '¿De qué año quieres el precio?',
        (2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014))
st.plotly_chart(sp.px_precio_diario(año), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
st.markdown("- A veces, el precio es cercano a cero o incluso cero, debido a la producción de energía renovable, que no es constante.")