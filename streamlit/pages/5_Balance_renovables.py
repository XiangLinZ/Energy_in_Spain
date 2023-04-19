import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp
import src.biblioteca as bb

st.write("Título")
"---"
st.markdown("¿Qué tipo de gráfica quieres?")
col1, col2, col3 = st.columns([1,1,5])
grafica = ""
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
elif grafica == "sun":
    st.plotly_chart(sp.px_porcentage_renovables_sunburst())
else:
    pass
st.write("Explicación energías")
st.write("Explicación gráfica")



st.write("Título")
"---"
st.write("Explicación gráfica")
energias = st.multiselect(
    '¿Qué energías quieres visualizar?',
    bb.tipos_energia,
    ['Carbón', 'Ciclo combinado', "Cogeneración"])
st.plotly_chart(sp.px_balance_renovables(energias))