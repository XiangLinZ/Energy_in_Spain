import streamlit as st

# Configuración de la página en ancho completo
st.set_page_config(layout="wide")

# Importamos las funciones de visualización
import sys
sys.path.append("../")
import src.soporte as sp

# Título de la sección de Generación Energética
st.write("<h1 style='text-align: center;'>Generación Energética</h1>", unsafe_allow_html=True)
"---"

# Descripción de la generación energética
st.markdown("###### La generación energética viene en unidades de MW/mes y representa el total de energía generada en España.")

# Gráfico de la generación energética
st.plotly_chart(sp.px_generado(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Detalles sobre la generación energética
st.markdown("- No hay tendecia en los últimos 10 años, es decir, España no ha aumentado su generación energética.")
st.markdown("- Bajada de generación energética en primavera del 2020 que coincide con el confinamiento del COVID-19.")

# Título de la sección de Pérdidas por Transporte
st.write("<h2 style='text-align: center;'>Pérdidas por Transporte</h2>", unsafe_allow_html=True)
"---"

# Descripción de las pérdidas por transporte
st.markdown("###### Las pérdidas por transporte se refieren al porcentaje de energía que se disipa o se pierde durante la transmisión y distribución a través de las redes eléctricas.")

# Gráfico de las pérdidas por transporte
st.plotly_chart(sp.px_perdidas(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Detalles sobre las pérdidas por transporte
st.markdown("- Ligera tendencia ascendente posiblemente debido al envejecimiento de la infraestructura.")
st.markdown("- La bajada en las pérdidas energéticas en otoño de 2014 pueden deberse a mejoras de infraestructura o condiciones climáticas favorables.")
st.markdown("- En verano hay menor pérdida debido a mejores condiciones climáticas, lo que produce menos averías.")
