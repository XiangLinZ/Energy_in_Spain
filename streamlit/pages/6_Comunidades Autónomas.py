import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página en centrado
st.set_page_config(layout="centered")


# Título de la sección evolución de las ccaa
st.write("<h1 style='text-align: center;'>Evolución de las CCAA</h1>", unsafe_allow_html=True)
"---"
st.markdown("###### Serie temporal donde podemos ver cuánta energía y qué porcentage de esta es renovable de cada CCAA.")

# Creación de objeto tipo Tableau a través de una url
html_temp = """
<div class='tableauPlaceholder' id='viz1681998278083' 'position: absolute; Top:50%; Bot50%;'>
    <noscript>
        <a href='#'>
            <img alt='Presentación ' src='https://public.tableau.com/static/images/Re/Renovables_CCAA/Presentacin/1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='Renovables_CCAA&#47;Presentacin' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https://public.tableau.com/static/images/Re/Renovables_CCAA/Presentacin/1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='es-ES' />
        <param name='filter' value='publish=yes' />
    </object>
</div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1681998278083');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 800 ) {
        vizElement.style.width='800px';
        vizElement.style.height='827px';
    } else if ( divElement.offsetWidth > 500 ) {
        vizElement.style.width='800px';
        vizElement.style.height='827px';
    } else {
        vizElement.style.width='100%';
        vizElement.style.height='727px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
"""

# Llamada a la gráfica de Tableau
components.html(html_temp, width = 850, height = 850, scrolling = False)

# Detalles interesantes de la gráfica
st.markdown("- Comunidades como Galicia, Castilla y León, Aragón y en los últimos años Andalucía, producen bastante energía y además están por encima de la media.")
st.markdown("- Por otro lado, Catalunya, Valencia y Extrmadura, también producen bastante energía, pero el porcentaje de renovables en esta es menor.")