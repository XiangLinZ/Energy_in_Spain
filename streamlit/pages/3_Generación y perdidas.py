import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Generación Energética")
"---"
st.markdown("###### La generación energética viene en unidades de MW/mes")
st.plotly_chart(sp.px_generado())
st.markdown("- No hay tendecia en los últimos 10 años.")

st.title("Perdidas por transporte")
"---"
st.markdown("###### Los datos están agrupados por meses y representan el porcentage del total generado.")
st.plotly_chart(sp.px_perdidas())
st.markdown("- Ligera tendencia ascendente.")
st.markdown("- Picos en inviernos y bajadas en verano.")
