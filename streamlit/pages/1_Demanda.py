import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

año = st.slider("¿De qué año quieres la demanda?", 2013, 2023, 2023)
st.plotly_chart(sp.px_demanda(año))