import streamlit as st
import pickle

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Renovables frente a no renovables")
"---"
st.markdown("- Energía renovable: Energía que se obtiene a partir de fuentes naturales virtualmente inagotables.")
st.markdown("- Energía no renovable: Fuentes de energía que se encuentran en la naturaleza en cantidades limitadas.")
with open(f"../data/visualizacion/px_evo_reno.pkl", "rb") as evo_reno:
    df = pickle.load(evo_reno)
mean_value_reno = df["percentage_Renovable"].mean()*100
st.markdown("###### El porcentage medio de energía renovable y no renovable generado en España en los últimos 10 años.")
col1, col2 = st.columns(2)
with col1:
    st.metric(label = "Porcentaje renovable", value = round(mean_value_reno,2))
with col2:
    st.metric(label = "Porcentaje no renovable", value = round(100-mean_value_reno, 2))
st.markdown("- En 2019, la media mundial se situaba en torno el 11%.")

st.header("Evolución de las energías renovables")
"---"
st.markdown("###### Porcentaje de energía generada por España renovable y no renovable en los últimos años.")
st.plotly_chart(sp.px_evo_reno())
st.markdown("- Ligerera tendencia en las energías renovables.")
st.markdown("- Bajadas por otoño debido a la inestabilidad de las energías renovables.")
