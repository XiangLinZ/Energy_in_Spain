import streamlit as st

st.set_page_config(layout="wide")

import sys
sys.path.append("../")
import src.soporte as sp

st.write("<h1 style='text-align: center;'>Generación Energética</h1>", unsafe_allow_html=True)
"---"
st.markdown("###### La generación energética viene en unidades de MW/mes")
st.plotly_chart(sp.px_generado(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
st.markdown("- No hay tendecia en los últimos 10 años.")
st.markdown("- Bajada en primavera del 2020 debido al confinamiento del COVID-19.")

st.write("<h2 style='text-align: center;'>Pérdidas por Transporte</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### Los datos están agrupados por meses y representan el porcentage del total generado.")
st.plotly_chart(sp.px_perdidas(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
st.markdown("- Ligera tendencia ascendente posiblemente debido al envejecimiento de la infraestructura.")
st.markdown("- En verano hay menor pérdida debido a mejores condiciones climáticas, lo que produce menos averías.")
