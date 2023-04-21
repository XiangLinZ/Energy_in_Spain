# 10 Años de energía en España
---
![portada](images/imagen_verde.jpg)
---
# Introducción
Cuando se habla de "energéticas en España", se hace referencia a la producción, distribución y comercialización de energía en el país, ya sea en forma de electricidad, gas o petróleo.

Este es un tema complejo que involucra aspectos técnicos, económicos y políticos, y está sujeto a volatilidad debido a factores externos como cambios en el mercado energético internacional, políticas gubernamentales y desastres naturales, entre otros. 

Por lo tanto, es crucial mantenerse informado sobre las últimas novedades y eventos relacionados con el sector energético en España, con el fin de comprender cómo pueden afectar a la economía del país y a la vida cotidiana de sus habitantes. 

Otro aspecto importante y para mí interesantes son las energías renovables. Las energías renovables son vitales para un futuro sostenible, ya que son una fuente de energía limpia e inagotable que contribuye a mitigar el cambio climático y garantizar la seguridad energética. 

Es por ello que he decidido profundizar en este tema para obtener una visión más completa y actualizada de la situación energética en España.

---
# Objetivos
- Investigar diferentes fuentes de información y seleccionar las más completas.
- Preparar los datos para visualizar posterirmente además de entrenar un modelo predictivo.
- Entrenar diversos modelos predictivos sobre la demanda real y quedándonos con el modelo que más se ajuste a nuestras preferencias.
- Realizar un análisis descriptivo de los datos e investigar e inferir en la naturaleza de estos.
- Crear un Streamlit como base para presentación de las conclusiones.

---
# Proceso
El objetivo principal de este proyecto es realizar un análisis descriptivo de los datos relacionados con la producción y demanda de energía en España.

### Recolección de datos

- Llamadas a la API "REData": Se obtendrán los datos de la API proporcionada por Red Eléctrica Española (REE), que contiene información relevante sobre la producción y demanda de energía en España.

### Tratamiento y limpieza de datos

- Limpieza y transformación de datos: Se realizará la limpieza y transformación de los datos obtenidos para adecuarlos a una estructura o formato deseado, preparándolos para su análisis y visualización.

### Análisis descriptivo

- Estudio y análisis de la naturaleza de los datos: Se realizará un análisis exploratorio de los datos obtenidos, utilizando posibles visualizaciones y técnicas de interpretación para comprender mejor su significado y patrones.

- Investigación de datos anómalos: Se investigarán los periodos en los que los datos presenten comportamientos anómalos o atípicos, con el fin de entender las posibles causas detrás de estos patrones y su impacto en los resultados del análisis.

### Modelo predictivo

- Construcción de un modelo predictivo de serie temporal: Se desarrollará un modelo de serie temporal para predecir la demanda de energía en base a los datos disponibles, buscando acercarse a los resultados proporcionados por REE.

### Visualización con Streamlit

- Creación de una mini app con Streamlit: Se utilizará la herramienta Streamlit para crear una interfaz de usuario amigable y accesible, en la cual se mostrarán los resultados del análisis descriptivo y las predicciones del modelo, para facilitar su visualización y comprensión.

---
# Modelo predictivo
- Modelo: ARIMA
- Orden estacional: (0, 1, 0, 2)
- Margen de error: 4'85%
---
# Streamlit
- He realizado un streamlit donde se analiza y se estudian todos los datos, además de las conclusiones y motivos de por qué los datos se comportan de esa manera. Lo puedes encontrar aquí.
---
# Herramientas
### He usado diversas herramientas en este proyecto con distintos fines, aquí enumero las herramientas, junto a una pequeña descripción de estas.

- [Numpy](https://numpy.org/): Es una biblioteca de Python para trabajar con matrices y arreglos multidimensionales.
- [Pandas](https://pandas.pydata.org/): Es una biblioteca de software libre para el lenguaje de programación Python destinada a manipulación y análisis de datos.

- [Matplotlib](https://matplotlib.org/): Es una biblioteca de Python para la generación de gráficos y visualizaciones.

- [Seaborn](https://seaborn.pydata.org/): Biblioteca de Python para la visualización de datos basada en matplotlib.

- [Random](https://docs.python.org/3/library/random.html): Una biblioteca de Python que permite trabajar con números aleatorios.

- [Pickle](https://docs.python.org/3/library/pickle.html): Biblioteca de Python que permite serializar y deserializar objetos de Python.

- [Tqdm](https://github.com/tqdm/tqdm): Es una biblioteca de Python para mostrar una barra de progreso en bucles y operaciones iterables.

- [Scikit-learn (sklearn)](https://scikit-learn.org/stable/) es una biblioteca de aprendizaje automático de código abierto para Python. Proporciona herramientas simples y eficientes para la minería y análisis de datos, así como para la construcción de modelos de aprendizaje automático y la evaluación de su rendimiento.