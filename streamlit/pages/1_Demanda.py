import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Demanda Energética")
"---"
st.markdown("###### La demanda energética española es a nivel nacional, es decir, esta demanda engloba diversos ámbitos, como el doméstico, insdustrial, alumbrado público, transporte, etc... Y esta demanda viene en unidades de MW.")

año = st.slider("¿De qué año quieres la demanda?", 2013, 2023, 2023)
st.plotly_chart(sp.px_demanda(año))
st.markdown("En esta gráfica interactiva podemos analizar la demanda diaria en un año en MW, la línea negra representa la media de ese mismo año.")
st.markdown("Como dato interesante las caídas siempre están asociadas a los días de las semanas pertenecientes a Domingos")
st.markdown("Los hogares españoles consumen de media 9kW la hora, que multiplicado por el número de horages en españa en 2021 y pasándolo a MW nos da como resultado que el consumo doméstico español es en torno a 160.000MW la hora y eso equivale a un 20% de la demanda media.")

st.header("Demanda Real semanal")
"---"
st.markdown("###### La demanda real representa las necesidades energéticas en tiempo real y esta se representa en intervalos de 10 minutos.")
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
st.markdown("En esta gráfica interactiva podemos analizar la demanda de la semana del día seleccionado en MW, la línea negra representa la media de esa semana.")
st.markdown("Podemos apreciar unas caídas reiteradas en los intervalos de las madrugadas. Y otras caidas más leves en las tardes.")
st.markdown("Por otro lado podemos ver dos picos de demanda tanto por las mañanas, como al anochecer.")
st.markdown("Por último podemos apreciar una bajada general en la demanda en los Sábados y Domingos.")

st.header("Demanda semanal por estaciones")
"---"
st.markdown("###### Por último vamos a comparar la demanda por estaciones")
st.plotly_chart(sp.px_demanda_estacion())
st.markdown("En esta gráfica tenemos la media de todas las semanas en los últimos 10 años por estación en MW.")
st.markdown("La línea discontínua negra representa la media.")
st.markdown("Como podemos ver, los contornos son semejantes pero distintos en cada estación.")