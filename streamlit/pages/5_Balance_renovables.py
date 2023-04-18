import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp
import src.biblioteca as bb

energias = st.multiselect(
    '¿Qué energías quieres visualizar?',
    bb.tipos_energia,
    ['Carbón', 'Ciclo combinado', "Cogeneración"])
st.plotly_chart(sp.px_balance_renovables(energias))