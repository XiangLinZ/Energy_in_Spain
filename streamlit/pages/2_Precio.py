import streamlit as st

import sys
sys.path.append("../")
import src.soporte as sp

st.title("Precio Energético")
"---"
st.markdown("###### Los datos que se analizan son referentes al precio energético español, esto, es el mercado mayorista, que después se desglosa en diferentes ámbitos, incluyendo a empresas de venta minorista, por lo que los precios no son iguales pero influyen al precio de la luz doméstica.")
st.plotly_chart(sp.px_precio_historico())
st.markdown("En el gráfico podemos apreciar que el precio es medianamente constante, a excepción de un anómalo pico que empieza a mediados de 2021.")
st.markdown("Estos picos en el precio energético pueden estar relacionados a...")

st.header("Análisis semanal")
"---"
st.markdown("###### En el análisis semanal, el precio energético vienen representados de forma horaria.")
año = st.slider("¿De qué año quieres la el precio?", 2014, 2023, 2023)
st.plotly_chart(sp.px_precio_diario(año))
st.markdown("Los valores son mucho más volátiles, mayormente se debe a la energía renovable, ya que esta, no es constante, y tiene altibajos en su producción.")
st.markdown("A veces, el precio es cercano a cero o incluso cero, esto se debe mayormente a momentos de baja demanda pero alta producción de renvables, cuando esto sucede, las productoras de energía renovable pueden llegar incluso a pagar para suministrar el excedente de energía a la red eléctrica, esto se debe a que no son capaces de almacenar tanta energía y sus baterías podrían ser dañadas, suponiendo un coste mayor.")