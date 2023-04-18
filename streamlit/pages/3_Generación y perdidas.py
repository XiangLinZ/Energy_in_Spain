import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.write("Título")
st.write("explicacion y generacion de las casas, comparación con la gráfica")
st.plotly_chart(sp.px_generado())

st.write("Título")
st.write("explicacion de las perdidas")
st.plotly_chart(sp.px_perdidas())