import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp
import src.biblioteca as bb


st.title("Balance Energías")
"---"
st.markdown("###### ¿Qué tipo de gráfica quieres?")
col1, col2, col3 = st.columns([1,1,5])
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
if grafica == "bar":
    st.plotly_chart(sp.px_porcentage_renovables_barplot())
    st.markdown("- Se aprecia mejor las diferencias entre energías.")
elif grafica == "sun":
    st.plotly_chart(sp.px_porcentage_renovables_sunburst())
    st.markdown("- Se aprecia mejor el porcentage de energía renovable frente a la no renovable.")
else:
    pass

st.markdown("##### ¿Mostrar descripción?")
col1a, col2a, col3a = st.columns([1,1,5])
mostrar = "no"
with col1a:
    if st.button('No'):
        mostrar = "no"
    else:
        pass
with col2a:
    if st.button('Sí'):
        mostrar = "si"
    else:
        pass
if mostrar == "si":
    st.subheader("Tipos de energías")
    "---"
    col1a, col2a, = st.columns(2)
    with col1a:
        st.markdown("###### Energías renovables")
        st.markdown("- Hidráulica: Convierte la cinética del agua en energía.")
        st.markdown("- Eólica: Convierte la cinética del viento en energía.")
        st.markdown("- Solar fotovoltáica: Convierte la luz solar en energía.")
        st.markdown("- Solar térmica: Convierte la luz en calor y luego en energía.")
        st.markdown("- Residuos renovables: Convierte los residuos naturales en energía.")
        st.markdown("- Hidroeólica: Combinación de eólica e hidráulica.")
        st.markdown("- Turbinación bombeo: Con energía sobrante, bombea agua y genera energía hidráulica.")
        st.markdown("- Otras renovables: Otras tecnologías como mareomotriz, hidrógeno, olas...")
    with col2a:
        st.markdown("###### Energías no renovables")
        st.markdown("- Nuclear: Conviertela energía de la fisión nuclear en energía.")
        st.markdown("- Carbón: Combustión del carbón.")
        st.markdown("- Motores diésel: Cobustión del diésel.")
        st.markdown("- Turbinación gas: Combustión de gas natural.")
        st.markdown("- Turbinación vapor: Calentamiento del agua para generar energía.")
        st.markdown("- Ciclo Combinado: Combinación de ambas tecnologías de turbinación.")
        st.markdown("- Cogeneración: Aprovecha el calor residual de otras energías no renovables.")
        st.markdown("- Residuos no renovables: Convierte los residuos humanos en energía.")
else:
    pass    

st.header("Evolución de cada energía")
"---"
st.markdown("###### Evolución por tipo de energía por meses en MW")
energias = st.multiselect(
    '¿Qué energías quieres visualizar?',
    bb.tipos_energia,
    ['Carbón', 'Ciclo combinado', "Cogeneración"])
st.plotly_chart(sp.px_balance_renovables(energias))
st.markdown("- Se opta por el ciclo combinado como alternativa del carbón.")

st.header("Emisiones de CO2")
"---"
st.markdown("###### Emisiones de residuos directos de CO2 de cada energía no renovable, estos valores están en T/mes.")
st.plotly_chart(sp.px_emisiones())
st.markdown("- Decrecimiento del carbón.")
st.markdown("- Crecimiento del ciclo combinado como alternativa del carbón.")