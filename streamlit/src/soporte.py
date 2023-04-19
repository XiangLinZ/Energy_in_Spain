######## Visualizacion
import pickle

import plotly.express as px
import plotly.graph_objects as go


def px_demanda(año):
    """
    Esta función carga datos de demanda de energía eléctrica en formato pickle,
    filtra los datos para el año especificado, calcula el valor promedio de la demanda,
    y genera una visualización de la demanda de energía eléctrica en un gráfico de línea.
    
    Args:
        año (int): El año para el cual se desea obtener la visualización de la demanda.
        
    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de la demanda de energía eléctrica.
    """
    with open(f"../data/visualizacion/px_demanda.pkl", "rb") as demanda:
        df = pickle.load(demanda)

    df_year = df[df["Fecha"].dt.year == int(año)]
    mean_value = df_year["Demanda en MW"].mean()

    fig = px.line(df_year, x = "Fecha", y = "Demanda en MW", line_group = None)
    
    fig.add_shape(go.layout.Shape(
        type = "line",
        x0 = df_year["Fecha"].iloc[0],
        y0 = mean_value,
        x1 = df_year["Fecha"].iloc[-1],
        y1 = mean_value,
        line = dict(color = "#00072D", width = 2, dash = "dot")))

    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor ="#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_demanda_real(año, semana):
    """
    Esta función carga datos de demanda de energía eléctrica en tiempo real en formato pickle,
    filtra los datos para el año y semana especificados, calcula el valor promedio de la demanda real,
    y genera una visualización de la demanda real, programada y prevista en un gráfico de línea utilizando
    Plotly Express.
    
    Args:
        año (int): El año para el cual se desea obtener la visualización de la demanda real.
        semana (int): El número de semana para el cual se desea obtener la visualización de la demanda real.
        
    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de la demanda real, programada y prevista.
    """
    with open(f"../data/visualizacion/px_demanda_real.pkl", "rb") as demanda_real:
        df = pickle.load(demanda_real)

    df_year2 = df[df["Fecha"].dt.year == int(año)]
    df_week2 = df_year2[df_year2["Fecha"].dt.isocalendar().week == int(semana)]
    mean_value = df_week2["Demanda real en MW"].mean()
    fig = px.line(
                df_week2,
                x = "Fecha",
                y = ["Demanda real en MW", "Demanda programada en MW", "Demanda prevista en MW"],
                color_discrete_sequence = ["blue", "red", "green"])
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df_week2["Fecha"].iloc[0],
            y0 = mean_value,
            x1 = df_week2["Fecha"].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
     
    return fig


def px_demanda_estacion():
    """
    Esta función carga datos de demanda de energía eléctrica clasificados por estación del año en formato pickle,
    calcula el valor promedio de la demanda para la estación de verano, y genera una visualización de la demanda
    por estación del año en un gráfico de línea utilizando Plotly Express.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de la demanda por estación del año.
    """
    with open(f"../data/visualizacion/px_demanda_estacion.pkl", "rb") as demanda_estacion:
        df = pickle.load(demanda_estacion)
    mean_value = df["Verano"].mean()
    fig = px.line(
            df,
            x = "Día",
            y = ["Primavera", "Verano", "Otoño", "Invierno"],
            color_discrete_map = {"Primavera":"green", "Verano":"red", "Otoño":"orange", "Invierno":"royalblue"})
    fig.update_layout(
        xaxis = dict(
            tickvals = [87+ (144*n) for n in range(0,7)],
            ticktext = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]),
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df["Día"].iloc[0],
            y0 = mean_value,
            x1 = df["Día"].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    return fig


def px_precio_historico():
    """
    Esta función carga datos de precios históricos de energía eléctrica en formato pickle,
    y genera una visualización de los precios históricos en un gráfico de línea utilizando Plotly Express.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de los precios históricos.
    """
    with open(f"../data/visualizacion/px_precio_historico.pkl", "rb") as precios_historico:
        df = pickle.load(precios_historico)
    fig = px.line(df, x = "Fecha", y = "Precio mayorista en €/MWh", line_group = None)

    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_precio_diario(año):
    with open(f"../data/visualizacion/px_precio_diario.pkl", "rb") as precio_diario:
        df = pickle.load(precio_diario)
    
    df_year = df[df["Fecha"].dt.year == int(año)]
    mean_value = df_year["Precio mayorista en €/MWh"].mean()
    fig = px.line(df_year, x = "Fecha", y = "Precio mayorista en €/MWh", line_group = None)
    
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df_year["Fecha"].iloc[0],
            y0 = mean_value,
            x1 = df_year["Fecha"].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor ="#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_porcentage_renovables_barplot():
    """
    Esta función carga datos de precios diarios de energía eléctrica en formato pickle para un año específico,
    y genera una visualización de los precios diarios en un gráfico de línea utilizando Plotly Express.
    
    Args:
        año (int): Año para el cual se desean visualizar los precios diarios.
        
    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de los precios diarios.
    """
    with open(f"../data/visualizacion/px_porcentage_renovables.pkl", "rb") as porcentage_renovables:
        df = pickle.load(porcentage_renovables)

    fig = px.bar(
        df,
        x = "Energia",
        y = "Porcentage",
        color = "Tipo",
        color_discrete_map = {"Renovable": "#44CF6C", "No Renovable": "#0E7C7B"})

    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_porcentage_renovables_sunburst():
    """
    Esta función carga datos de porcentaje de energía renovable en formato pickle y genera una visualización
    en forma de gráfico de sol (sunburst) utilizando Plotly Express.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización del porcentaje de energía renovable.
    """
    with open(f"../data/visualizacion/px_porcentage_renovables.pkl", "rb") as porcentage_renovables:
        df = pickle.load(porcentage_renovables)

    fig = px.sunburst(
        df,
        path = ["Tipo", "Energia"],
        values = "Porcentage",
        color = "Tipo",
        color_discrete_map = {"Renovable": "#44CF6C", "No Renovable": "#0E7C7B"})
    
    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))

    return fig


def px_balance_renovables(energias):
    """
    Esta función carga datos de balance de energías renovables en formato pickle y genera una visualización
    en forma de gráfico de línea utilizando Plotly Express.
    
    Args:
        energias (list): Una lista de strings que contiene los nombres de las columnas de energías a visualizar en el gráfico.
        
    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización del balance de energías renovables.
    """
    with open(f"../data/visualizacion/px_balance_renovables.pkl", "rb") as balance_renovables:
        df = pickle.load(balance_renovables)
    fig = px.line(
        df,
        x = "Fecha",
        y = energias,
        color_discrete_map = {
        "Turbinación bombeo": "blue", "Nuclear": "green", "Ciclo combinado": "brown",
        "Carbón": "black", "Turbina de gas": "orange", "Motores diésel": "gold", "Turbina de vapor": "cyan",
        "Fuel + Gas": "pink", "Cogeneración": "grey", "Residuos no renovables": "purple", "Hidráulica": "royalblue",
        "Eólica": "lightblue", "Solar fotovoltaica": "yellow", "Solar térmica": "red", "Otras renovables": "violet",
        "Residuos renovables": "yellowgreen", "Hidroeólica": "seashell"})
    
    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_evo_reno():
    """
    Esta función carga datos de evolución de energías renovables en formato pickle y genera una visualización
    en forma de gráfico de líneas utilizando Plotly y Go.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de la evolución de energías renovables.
    """
    with open(f"../data/visualizacion/px_evo_reno.pkl", "rb") as evo_reno:
        df = pickle.load(evo_reno)
    mean_value = df["percentage_Renovable"].mean()*100

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x = df["mes_y_año"], y = (df["percentage_Renovable"]*100),
        hoverinfo = "x+y",
        mode = "lines",
        line = dict(width = 0.5, color = "#44CF6C"),
        stackgroup = "one",
        name = "Renovable"))
    
    fig.add_trace(go.Scatter(
        x = df["mes_y_año"], y = (df["percentage_No renovable"]*100),
        hoverinfo = "x+y",
        mode = "lines",
        line = dict(width = 0.5, color = "#0E7C7B"),
        stackgroup = "one",
        name = "No Renovable"))
    
    fig.add_shape(go.layout.Shape(
                type = "line",
                x0 = df["mes_y_año"].iloc[0],
                y0 = mean_value,
                x1 = df["mes_y_año"].iloc[-1],
                y1 = mean_value,
                line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        yaxis_range = (0, 100),
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))

    return fig


def px_emisiones():
    """
    Esta función carga datos de emisiones de energías no renovables en formato pickle y genera una visualización
    en forma de gráfico de líneas utilizando Plotly y Go.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de las emisiones de energías no renovables.
    """
    with open(f"../data/visualizacion/px_emisiones.pkl", "rb") as emisiones:
        df = pickle.load(emisiones)

    fig = px.line(
        df,
        x = "Fecha",
        y = ["Carbón", "Motores diésel", "Turbina de gas", "Turbina de vapor", "Ciclo combinado", "Cogeneración", "Residuos no renovables"])
    
    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_perdidas():
    """
    Esta función carga datos de pérdidas de energía en formato pickle y genera una visualización en forma de gráfico de líneas
    utilizando Plotly y Go.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de las pérdidas de energía.
    """
    with open(f"../data/visualizacion/px_perdidas.pkl", "rb") as perdidas:
        df = pickle.load(perdidas)

    mean_value = df["Porcentage"].mean()

    fig = px.line(df, x = "Fecha", y = "Porcentage", line_group = None)
    
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df["Fecha"].iloc[0],
            y0 = mean_value,
            x1 = df["Fecha"].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor = "#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig


def px_generado():
    """
    Esta función carga datos de generación de energía en formato pickle y genera una visualización en forma de gráfico de líneas
    utilizando Plotly y Go.
    
    Args:
        None

    Returns:
        fig (plotly.graph_objects.Figure): La figura generada con la visualización de la generación de energía.
    """
    with open(f"../data/visualizacion/px_generado.pkl", "rb") as generado:
        df = pickle.load(generado)
        
    mean_value = df["Generación en MW"].mean()

    fig = px.line(df, x = "Fecha", y = "Generación en MW", line_group = None)

    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df["Fecha"].iloc[0],
            y0 = mean_value,
            x1 = df["Fecha"].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))

    fig.update_layout(
        plot_bgcolor = "#E1D5D7",
        paper_bgcolor ="#F7EBEC",
        font = dict(family = "Arial", color = "#00072D"))
    
    return fig