import streamlit as st

# Configuración de la página en ancho completo
st.set_page_config(layout="wide")

# Importamos las funciones de visualización
import sys
sys.path.append("../")
import src.soporte as sp
import src.biblioteca as bb

# Título de la sección de Composición del Mix Energético
st.write("<h1 style='text-align: center;'>Composición del Mix Energético</h1>", unsafe_allow_html=True)
"---"

# Explicación del mix energético
st.markdown("###### El mix energético se refiere a la combinación o proporción de diferentes fuentes de energía que se utilizan para abastecer las necesidades energéticas de España.")

# Selector del tipo de gráfica
st.write("<h5 style='text-align: center;'>¿Qué tipo de gráfica quieres?</h5>", unsafe_allow_html=True)
relleno, col1, col2, relleno2 = st.columns([5,1,1,5])
grafica = "bar"
with col1:
    if st.button('Barplot'):
        grafica = "bar"
    else:
        pass
with col2:
    if st.button('Sunburst'):
        grafica = "sun"
    else:
        pass

# Gráficas que se seleccionan dependiendo del output anterior
if grafica == "bar":
    st.plotly_chart(sp.px_porcentage_renovables_barplot(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
    st.markdown("- Se aprecia mejor las diferencias entre las distintas energías relevantes y las no tan relevantes.")
elif grafica == "sun":
    st.plotly_chart(sp.px_porcentage_renovables_sunburst(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
    st.markdown("- Se aprecia mejor el porcentage de energía renovable frente a la no renovable.")

# Detalles sobre el mix energético
st.markdown("- La energía nuclear sigue siendo una parte importante de la energía generada por España, una quinta parte del total.")
st.markdown("- España apuesta fuerte por la energía eólica debido a que se están realizando bastantes avances en su tecnología y está situada en un excelente punto geográfico con viento constante.")
st.markdown("- La energía solar no es tan relevante debido a cambios en la política energética, un avance más lento en su tecnología y un mayor coste de inversión.")

# Selector para mostrar las descripciones de cada energía y la información de estas.
st.write("<h5 style='text-align: center;'>¿Mostrar explicación de los tipos de energías?</h5>", unsafe_allow_html=True)

rellenoa, col1a, col2a, relleno2a = st.columns([10,1,1,10])
mostrar = "no"
with col1a:
    if st.button('No'):
        mostrar = "no"

with col2a:
    if st.button('Sí'):
        mostrar = "si"
if mostrar == "si":
    st.subheader("Tipos de energías")
    "---"
    col1a, col2a, = st.columns(2)
    with col1a:
        st.markdown("###### Energías renovables")
        st.markdown("- Hidráulica: Convierte la cinética del agua en energía eléctrica.")
        st.markdown("- Eólica: Convierte la cinética del viento en energía eléctrica.")
        st.markdown("- Solar fotovoltáica: Convierte la luz solar en energía eléctrica.")
        st.markdown("- Solar térmica: Convierte la luz en energía térmica y posteriormente en energía eléctrica.")
        st.markdown("- Residuos renovables: Mediante la combustión de residuos naturales se obtiene energía eléctrica.")
        st.markdown("- Hidroeólica: Combinación de eólica e hidráulica.")
        st.markdown("- Turbinación bombeo: Con energía sobrante, se bombea agua y posteriormente se genera energía hidráulica con esta.")
        st.markdown("- Otras renovables: Otras tecnologías como mareomotriz, hidrógeno, geotérmica, oleaje...")
    with col2a:
        st.markdown("###### Energías no renovables")
        st.markdown("- Nuclear: Conviertela energía de la fisión nuclear en energía eléctrica.")
        st.markdown("- Carbón: Combustión del carbón.")
        st.markdown("- Motores diésel: Cobustión del diésel.")
        st.markdown("- Turbinación gas: Combustión de gas natural.")
        st.markdown("- Turbinación vapor: Calentamiento del agua para generar energía.")
        st.markdown("- Ciclo Combinado: Combinación de ambas tecnologías de turbinación.")
        st.markdown("- Cogeneración: Aprovecha el calor residual de otras energías no renovables.")
        st.markdown("- Residuos no renovables: Convierte los residuos humanos en energía.")
else:
    pass    

# Título de la sección de evolución energética 
st.write("<h2 style='text-align: center;'>Evolución Energética</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### Evolución por tipo de energía por meses en MW")

# Selector de las energías a visualizar
energias = st.multiselect(
    '¿Qué energías quieres visualizar?',
    bb.tipos_energia,
    ['Carbón', 'Ciclo combinado'])

# Gráfico de la evolución de la energía generada de los tipos seleccionados
st.plotly_chart(sp.px_balance_renovables(energias), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Detalles sobre la evolución de algunos tipos
st.markdown("- Se opta por el ciclo combinado como alternativa del carbón.")
st.markdown("- Las principales energías renovables producen más en primavera haciendo que se recurra menos a las no renovables en esos periodos.")

# Título de la sección de emisiones CO2
st.write("<h2 style='text-align: center;'>Emisiones de CO2</h2>", unsafe_allow_html=True)
"---"

# Explicación de las emisiones
st.markdown("###### Se refiere a las emisiones directas de dióxido de carbono (CO2) producidas por cada fuente de energía no renovable, las cuales se expresan en toneladas por mes (T/mes).")

# Gráfica de las emisiones de CO2
st.plotly_chart(sp.px_emisiones(), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Detalles sobre las emisiones de CO2
st.markdown("- El ciclo combinado es una buena alternativa del carbón porque emite menos CO2 produciendo la misma energía.")
st.markdown("- En 2021 España se situaba en el puesto 159 de 184 países en el ranking de emisiones de CO2.")