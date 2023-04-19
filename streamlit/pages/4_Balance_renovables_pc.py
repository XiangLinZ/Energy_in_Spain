import datetime
import streamlit as st
import pickle

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Renovables frente a no renovables")
"---"
with open(f"../data/visualizacion/px_evo_reno.pkl", "rb") as evo_reno:
    df = pickle.load(evo_reno)
mean_value_reno = df["percentage_Renovable"].mean()*100
st.markdown("###### El porcentage medio de energía renovable y no renovable generado en España en los últimos 10 años.")
col1, col2 = st.columns(2)
with col1:
    st.metric(label = "Energía renovable", value = round(mean_value_reno,2))
with col2:
    st.metric(label = "Energía no renovable", value = round(100-mean_value_reno, 2))
st.markdown("Estos valores representan qué porcentage de toda la energía generada en España, en 2019, la media mundial se situaba en torno el 11%, por lo que España supera con creces la media mundial.")

st.header("Evolución de las energías renovables")
"---"
st.markdown("###### Los datos representan qué porcentaje de energía generada por España es renovable o no por meses en los años.")
st.plotly_chart(sp.px_evo_reno())
st.markdown("Podemos apreciar una ligerera tendencia en el crecimiento del porcentage de las energías renovables.")

st.header("Emisiones de CO2")
"---"
st.markdown("###### Emisiones de residuos directos de CO2 de cada energía no renovable, estos valores están en T/mes.")
st.plotly_chart(sp.px_emisiones())
st.markdown("Podemos apreciar un decrecimiento del carbón, y esto se debe a que España cada vez más opta por otras alternativas menos contaminantes. Por otro lado, dentro de su evolución, podemos ver un pequeño aumento pasagero en el verano de 2022, que las posibles causas externas puede ser el conflicto Ukrania-Rusia.")