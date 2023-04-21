import streamlit as st
st.set_page_config(layout="wide")

st.write("<h1 style='text-align: center;'>10 Años de energía en España</h1>", unsafe_allow_html=True)
"---"
st.image("../images/imagen_verde2.jpg", use_column_width = True)

st.write("Cuando se habla de 'energéticas en España', se refiere a las empresas encargadas de la producción, distribución y comercialización de energía en el país, ya sea eléctrica, gas o petróleo. Este es un tema que puede resultar complicado, ya que involucra aspectos técnicos, económicos y políticos.")
st.write("Además, es un tema volátil debido a que está influenciado por factores externos que pueden afectar su estabilidad, como los cambios en el mercado energético internacional, las políticas gubernamentales, los desastres naturales, entre otros.")
st.write("Por lo tanto, es importante estar informado sobre las últimas novedades y eventos relacionados con el sector energético en España, con el fin de entender mejor cómo estos pueden afectar a la economía del país y a la vida cotidiana de sus habitantes.")
st.write("Otro aspecto importante son las energías renovables, las cuales son vitales para un futuro sostenible, ya que son una fuente de energía limpia e inagotable que contribuye a mitigar el cambio climático y garantizar la seguridad energética.")
st.write("Es por eso que decidí indagar más en este tema, para poder tener una visión más completa y actualizada de la situación energética en España.")
"---"
st.write("<h2 style='text-align: center;'>Proceso</h2>", unsafe_allow_html=True)
"---"
st.markdown("###### Este proyecto tiene como objetivo principal realizar un análisis descriptivo de los datos sobre energéticas.")
st.markdown('- Recolección de datos: Mediante llamadas a la API "REData". REData es una API de Red Eléctrica Española, que tiene disponible diversos datos relacionados con la producción y demanda de energía en España.')
st.markdown("- Tratamiento y limpieza de datos: Limpiar y transformar los datos para tenerlos con una estructura o formato deseada, para después realizar modelos predictivos o visualizar estos datos.")
st.markdown("- Análisis descriptivo: Estudiar y analizar la naturaleza de los datos, mediante posibles visualizaciones e interpretar estos resultados.")
st.markdown("- Realizar un modelo predictivo: En este caso una serie temporal sobre la demanda e intentar acercarme a los resultados de REE.")
st.markdown("- Streamlit: Mostrar los resultados junto al análisis en una mini app con la herramienta Streamlit para tener así una interfaz más amigable y accesible.")
"---"
