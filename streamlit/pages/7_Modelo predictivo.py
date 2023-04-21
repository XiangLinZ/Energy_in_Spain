import streamlit as st

st.set_page_config(layout="wide")

import sys
sys.path.append("../")
import src.soporte as sp

st.write("<h2 style='text-align: center;'>Modelo Predictivo</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### He entrenado un modelo predicitvo con los datos de la demanda para ver cuán cerca estarían mis predicciones de los valores reales.")
st.markdown("###### Se han hecho predicciones de 24 valores, es decir 4 horas.")
st.plotly_chart(sp.px_prediccion(),config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
st.markdown("###### Características:")
st.markdown("- Modelo: ARIMA")
st.markdown("- Orden estacional: (0,1,0,2)")
st.markdown("- Margen de error: 4'85%")