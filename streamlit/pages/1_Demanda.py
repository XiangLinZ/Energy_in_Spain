import datetime
import streamlit as st

# Configuración de la página
st.set_page_config(layout="wide")

# Importación de módulos personalizados
import sys
sys.path.append("../")
import src.soporte as sp

# Título principal de la página
st.write("<h1 style='text-align: center;'>Demanda Energética</h1>", unsafe_allow_html=True)

# Separador
"---"

# Descripción de la demanda energética
st.markdown("###### La demanda energética es a nivel nacional y representa la cantidad de electricidad que es requerida para el uso residencial, comercial e industrial, entre otros sectores. Además viene en unidades de MW/día.")

# Columna para seleccionar el año de la demanda
col1, relleno = st.columns([1,4])
with col1:
    año = st.slider("¿De qué año quieres la demanda?", 2013, 2023, 2023)

# Gráfico de la demanda energética por año
st.plotly_chart(sp.px_demanda(año), config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Descripción de patrones de la demanda energética
st.markdown("- Las caídas siempre están asociadas a los días de las semanas pertenecientes a fines de semana, debido a la disminución de actividad humana.")
st.markdown("- La demanda es inferior en primavera y en otoño, debido al clima y las horas de luz entre otros factores.")

# Título de la demanda real semanal
st.write("<h2 style='text-align: center;'>Demanda Real Semanal</h2>", unsafe_allow_html=True)

# Separador
"---"

# Descripción de la demanda real
st.markdown("###### La demanda real se representa en intervalos de 10 minutos.")
st.markdown("- Demanda real: demanda energética real en ese momento.")
st.markdown("- Demanda programada: valores energéticos preparados para ese momento.")
st.markdown("- Demanda prevista: demanda prevista mediante modelo predictorio de España.")

# Selector de fecha para la demanda real
d = st.date_input(
    "Selecciona una fecha:",
    datetime.date(2023, 3, 1))
año_real = d.year
semana_real = d.isocalendar().week

# Gráfico de la demanda real semanal
try:
    st.plotly_chart(sp.px_demanda_real(año_real, semana_real),config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)
except:
    st.write(f"Lamentablemente, no se disponen de datos para la fecha {d}, los datos disponibles cubre el marco temporal desde 2014/01/06 hasta 2023/03/31.")

# Descripción de patrones de la demanda real
st.markdown("- Hay menos demanda por las madrugadas debido a los patrones de sueño.")
st.markdown("- Hay menor demanda por las tardes debido a descansos, mejor clima, horarios de trabajo y escuela, entre otros motivos.")
st.markdown("- Los fines de semana hay menos actividad laboral e industrial.")

# Título de la demanda estacional
st.write("<h2 style='text-align: center;'>Demanda Estacional</h2>", unsafe_allow_html=True)

# Separador
"---"

# Gráfica de comparación de la demanda por estación del año
st.markdown("###### Comparación de la media de todas las semanas en los últimos 10 años por estación en MW.")
st.plotly_chart(sp.px_demanda_estacion(),config={'displayModeBar': False, 'staticPlot': False, 'scrollZoom': False, 'editable': False},use_container_width=True)

# Descripción de las tendencias observadas en la demanda por estación del año
st.markdown("- En primavera hay menor demanda debido a un clima más templado y a mayores horas de luz.")
st.markdown("- En verano la demanda es mayor debido al calor y al turismo, por las noches es menor debido a mayores horas de luz y climas templados.")
st.markdown("- En otoño la demanda es mayor a la primavera debido a menores horas de luz.")
st.markdown("- En invierno la demanda es mayor debido a las menores temperaturas y menores horas de luz.")