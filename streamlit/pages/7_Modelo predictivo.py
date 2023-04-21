import streamlit as st

# Configuración de la página en ancho completo
st.set_page_config(layout="wide")

# Importamos las funciones de visualización
import sys
sys.path.append("../")
import src.soporte as sp

# Título de la sección de modelopredictivo
st.write("<h2 style='text-align: center;'>Modelo Predictivo</h2>", unsafe_allow_html=True)
"---"

# Explicación de la gráfica
st.markdown("###### He entrenado un modelo predicitvo con los datos de la demanda para ver cuán cerca estarían mis predicciones de los valores reales.")
st.markdown("###### Se han hecho predicciones de 24 valores, es decir 4 horas.")

# Gráficas comparando el modelo con el modelo de REE y los valores reales
st.plotly_chart(sp.px_prediccion(),config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Características del modelo
st.markdown("###### Características:")
st.markdown("- Modelo: ARIMA")
st.markdown("- Orden estacional: (0,1,0,2)")
st.markdown("- Margen de error: 4'85%")