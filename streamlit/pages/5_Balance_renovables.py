import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp
import src.biblioteca as bb

st.write("Título")
st.write("Explicación energías")
st.write("Explicación gráfica")
st.plotly_chart(sp.px_porcentage_renovables_barplot())
st.plotly_chart(sp.px_porcentage_renovables_sunburst())


st.write("Título")
st.write("Explicación gráfica")
energias = st.multiselect(
    '¿Qué energías quieres visualizar?',
    bb.tipos_energia,
    ['Carbón', 'Ciclo combinado', "Cogeneración"])
st.plotly_chart(sp.px_balance_renovables(energias))