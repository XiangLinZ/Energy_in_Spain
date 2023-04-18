import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.write("Título")
st.write("big numbers porcentaje medio ultimos 10 años")
st.write("explicacion gráfica")
st.plotly_chart(sp.px_evo_reno())

st.write("Título")
st.write("Explicación gráfica")
st.plotly_chart(sp.px_emisiones())