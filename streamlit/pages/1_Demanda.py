import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Demanda Energética")
"---"
st.markdown("###### La demanda energética es a nivel nacional, engloba diversos ámbitos y viene en unidades de MW.")

año = st.slider("¿De qué año quieres la demanda?", 2013, 2023, 2023)
st.plotly_chart(sp.px_demanda(año))
st.markdown("- Las caídas siempre están asociadas a los días de las semanas pertenecientes a Domingos.")

st.header("Demanda Real semanal")
"---"
st.markdown("###### La demanda real se representa en intervalos de 10 minutos.")
st.markdown("- Demanda real: demanda energética real en ese momento.")
st.markdown("- Demanda programada: valores energéticos preparados para ese momento.")
st.markdown("- Demanda prevista: demanda prevista mediante modelo predictorio de España.")
d = st.date_input(
    "Selecciona una fecha:",
    datetime.date(2023, 3, 1))
año_real = d.year
semana_real = d.isocalendar().week

try:
    st.plotly_chart(sp.px_demanda_real(año_real, semana_real))
except:
    st.write(f"Lamentablemente, no se disponen de datos para la fecha {d}, los datos disponibles cubre el marco temporal desde 2014/01/06 hasta 2023/03/31.")
st.markdown("- Hay menos demanda por madrugadas y por el medio día.")
st.markdown("- Hay más demanda por las mañanas y por las noches.")
st.markdown("- Hay menos demanda en los Sábados y Domingos.")

st.header("Modelo predictivo")
"---"
st.plotly_chart(sp.px_prediccion())
st.markdown("- Modelo: ARIMA")
st.markdown("- Margen de error: 4'85%")

st.header("Demanda semanal por estaciones")
"---"
st.markdown("###### Comparación de la demanda por estaciones")
st.plotly_chart(sp.px_demanda_estacion())
st.markdown("- En esta gráfica tenemos la media de todas las semanas en los últimos 10 años por estación en MW.")
st.markdown("- Los contornos son semejantes pero distintos en cada estación.")