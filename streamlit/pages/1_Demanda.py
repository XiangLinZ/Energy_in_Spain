import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.write("Título")
st.write("Intro")

año = st.slider("¿De qué año quieres la demanda?", 2013, 2023, 2023)
st.plotly_chart(sp.px_demanda(año))


st.write("Análisis Semanal de la demanda Real")

st.write("explicación")

d = st.date_input(
    "Selecciona una fecha:",
    datetime.date(2023, 3, 1))
año_real = d.year
semana_real= d.isocalendar().week

try:
    st.plotly_chart(sp.px_demanda_real(año_real, semana_real))
except:
    st.write(f"Lamentablemente, no se disponen de datos para la fecha {d}, los datos disponibles cubre el marco temporal desde 2014/01/06 hasta 2023/03/31.")


st.write("Análisis Semanal de la demanda por estaciones")

st.plotly_chart(sp.px_demanda_estacion())