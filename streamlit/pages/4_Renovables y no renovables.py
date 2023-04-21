import streamlit as st
import pickle

# Configuración de la página en ancho completo
st.set_page_config(layout="wide")

# Importamos las funciones de visualización
import sys
sys.path.append("../")
import src.soporte as sp

# Título de la sección de Energías Renovables
st.write("<h1 style='text-align: center;'>Energía Renovables</h1>", unsafe_allow_html=True)
"---"

# Imagen de fondo
st.image("../images/verde2b.jpg", use_column_width = True)

# Carga de datos y cálculo del promedio de energía renovable
with open(f"../data/visualizacion/px_evo_reno.pkl", "rb") as evo_reno:
    df = pickle.load(evo_reno)
mean_value_reno = df["percentage_Renovable"].mean()*100

# Título y contenido de porcentaje de energía renovable y no renovable
st.write("<h4 style='text-align: center;'>Porcentaje de energía Renovables y no Renovable en los últimos años</h4>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.write(f"<h5 style='text-align: center;'>Renovable</h5>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align: center;'>{round(mean_value_reno,2)}%</h2>", unsafe_allow_html=True)
with col2:
    st.write(f"<h5 style='text-align: center;'>No Renovable</h5>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align: center;'>{round(100-mean_value_reno, 2)}%</h2>", unsafe_allow_html=True)
# Descripción de energías renovables y no renovables
st.markdown("- Energía renovable: Energía que se obtiene a partir de fuentes naturales virtualmente inagotables.")
st.markdown("- Energía no renovable: Fuentes de energía que se encuentran en la naturaleza en cantidades limitadas.")
st.markdown("- En 2019, la media mundial se situaba en torno el 11% y la media europea en el 34%.")

# Título de la sección de Evolución de Renovables
st.write("<h2 style='text-align: center;'>Evolución de Renovables</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### Porcentaje de energía generada por España renovable y no renovable en los últimos años.")

# Gráfico de evolución de energías renovables y no renovables
st.plotly_chart(sp.px_evo_reno(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Detalles sobre la evolución de energías renovables
st.markdown("- Ligera tendencia creciente en las energías renovables.")
st.markdown("- Bajadas por otoño debido a la inestabilidad de las energías renovables.")
