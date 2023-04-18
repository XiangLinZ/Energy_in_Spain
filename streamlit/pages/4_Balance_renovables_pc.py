import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.plotly_chart(sp.px_evo_reno())
st.plotly_chart(sp.px_emisiones())