import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.write("Título")
st.write("explicacion")
st.plotly_chart(sp.px_precio_historico())

st.write("Análisis semanal")
st.write("Explicacion")
año = st.slider("¿De qué año quieres la el precio?", 2014, 2023, 2023)
st.plotly_chart(sp.px_precio_diario(año))