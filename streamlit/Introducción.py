import streamlit as st

st.title("10 Años de energía en España")
"---"
st.image("../images/energia_bombilla.jpg")

st.write("Las energéticas en españa son un tema complicado e incluso volátiles, y más aún con varios eventos que afectan este campo, por eso mismo, quise indagar un poco más en este tema.")
st.write("Por otro lado, otro ámbito interesante e importante para mí son las energías renovables, siempre he oido de estas, por lo que ahora tengo la oportunidad para aumentar mi entendimiento en este campo y así poder analizar el panorama de las energías renovables.")
"---"
st.header("Proceso")
"---"
st.markdown("###### Este proyecto tiene como objetivo principal realizar un análisis descriptivo de los datos sobre energéticas.")
st.markdown('- Recolección de datos: Mediante llamadas a la API "REData". REData es una API de Red Eléctrica Española, que tiene disponible diversos datos relacionados con la producción y demanda de energía en España.')
st.markdown("- Tratamiento y limpieza de datos: Limpiar y transformar los datos para tenerlos con una estructura o formato deseada, para después realizar modelos predictivos o visualizar estos datos.")
st.markdown("- Análisis descriptivo: Estudiar y analizar la naturaleza de los datos, mediante posibles visualizaciones e interpretar estos resultados.")
st.markdown("- Realizar un modelo predictivo: En este caso una serie temporal sobre la demanda e intentar aacercarme a los resultados de REE.")
st.markdown("- Streamlit: Mostrar los resultados junto al análisis en una mini app con la herramienta Streamlit para tener así una interfaz más amigable y accesible.")
"---"
