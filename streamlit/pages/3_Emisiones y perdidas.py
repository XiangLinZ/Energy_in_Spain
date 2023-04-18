import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.plotly_chart(sp.px_generado())

st.plotly_chart(sp.px_perdidas())