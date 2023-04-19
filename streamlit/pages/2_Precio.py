import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Precio Energético")
"---"
st.markdown("###### Los datos son referentes al precio energético nacional, influyen pero no son iguales al precio doméstico.")
st.plotly_chart(sp.px_precio_historico())
st.markdown("En primavera de 2021 hay un aumento por el encarecimiento del gas, seguido por el comflicto de Ukrania-Rusia.")


st.header("Análisis semanal")
"---"
st.markdown("###### En el análisis semanal, el precio energético vienen representados de forma horaria.")
año = st.slider("¿De qué año quieres la el precio?", 2014, 2023, 2023)
st.plotly_chart(sp.px_precio_diario(año))
st.markdown("Los valores son mucho más volátiles, mayormente se debe a la energía renovable, ya que esta, no es constante, y tiene altibajos en su producción.")
st.markdown("A veces, el precio es cercano a cero o incluso cero, esto se debe mayormente a momentos de baja demanda pero alta producción de renvables, cuando esto sucede, las productoras de energía renovable pueden llegar incluso a pagar para suministrar el excedente de energía a la red eléctrica, esto se debe a que no son capaces de almacenar tanta energía y sus baterías podrían ser dañadas, suponiendo un coste mayor.")