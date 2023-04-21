import streamlit as st

# Configuración de la página en ancho completo
st.set_page_config(layout="wide")

# Importación de módulos y funciones necesarias
import sys
sys.path.append("../")
import src.soporte as sp

# Título de la página y descripción del precio energético
st.write("<h1 style='text-align: center;'>Precio Energético</h1>", unsafe_allow_html=True)
"---"
st.markdown("###### El precio energético es el valor económico que se paga por la energía utilizada, ya sea electricidad, gas, petróleo u otras fuentes de energía y puede tener un impacto significativo en los costos de energía para consumidores y empresas.")

# Gráfica de precio energético histórico
st.plotly_chart(sp.px_precio_historico(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Descripción de las tendencias observadas en el precio energético
st.markdown("- En los 2 últimos años el precio ha llegado a multiplicarse hasta por 10 respecto a años anteriores.")
st.markdown("- Los precios son medianamente estables hasta primavera de 2021, que coincide con la crisis de escased de gas natural y la borrasca Filomena.")
st.markdown("- Otro factor importante en la primavera de 2021 es el aumento del precio por permisos de emisiones de CO2.")
st.markdown("- En primavera de 2022 inicia el conflicto Ukrania-Rusia, el cual dificulta la recuperación del precio eléctrico.")

# Título de la sección de análisis anual
st.write("<h2 style='text-align: center;'>Análisis Anual</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### En el análisis anual, el precio energético vienen representados de forma horaria.")

# Selección del año para el análisis anual
col1, relleno = st.columns([1,4])
with col1:
    año = st.selectbox(
        '¿De qué año quieres el precio?',
        (2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014))

# Gráfica de precio energético diario para el año seleccionado
st.plotly_chart(sp.px_precio_diario(año), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Descripción de las tendencias observadas en el precio energético diario
st.markdown("- A veces, el precio es cercano a cero o incluso cero, debido a la producción de energía renovable, que no es constante. Al no poder almacenar toda la energía en las baterías, puesto que podría ser dañino, las empresas renovables pagan por conectar el excedente a la red eléctrica.")
st.markdown("- Estos precios afectan de manera sutil al precio de luz doméstico, puesto que las empresas de venta al por menor pagan estos precios y realizan una media para vender después la electricidad.")