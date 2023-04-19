import datetime
import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Generación Energética")
"---"
st.markdown("###### La generación energética viene en unidades de MW, por otro lado, nustros datos vienen agrupados por es, es decir, los valores representados son la generación total de cada mes.")
st.plotly_chart(sp.px_generado())
st.markdown("En los datos podemos ver que no hay nigún tipo de tendecia, por lo que podemos entender que España no ha aumentado su produción eléctrica en los últimos 10 años.")

st.title("Perdidas por transporte")
"---"
st.markdown("###### Los datos de nuevo están agrupados por meses, y los valores están representados porcentualmente respecto a la energía total generada.")
st.markdown("###### Estos valores representa qué porcentage de energía se pierde debido al transporte de este mismo, es decir, la energía que se pierde en la distribución de esta o incluso a limitaciones tecnológicas, como a las propias leyes de la física, también pueden deberse a fallos técnicos o de manipulación.")
st.plotly_chart(sp.px_perdidas())
st.markdown("Podemos apreciar una ligera tendencia ascendente en la pérdida en el transporte.")
st.markdown("También es apreciable picos en inviernos y bajadas en torno a verano.")