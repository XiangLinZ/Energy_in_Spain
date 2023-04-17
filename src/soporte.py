import calendar
import pandas as pd
import numpy as np
import requests
import pickle

import plotly.express as px
import plotly.graph_objects as go

import sys
sys.path.append("../")
import src.biblioteca as bb

def balance():
    df_final = pd.DataFrame()
    years = [x for x in range(2013,2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f"https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["content"][0]["attributes"]["values"])).drop(["value", "percentage"], axis = 1)

            for n in range(len(respuesta["included"])):
                for numb in range(len(respuesta["included"][n]["attributes"]["content"])):

                    tipo = respuesta["included"][n]["attributes"]["content"][numb]["type"]

                    df_values = (pd.DataFrame(respuesta["included"][n]["attributes"]["content"][numb]["attributes"]["values"])).drop(["datetime"], axis = 1)

                    df_values.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                    df_fecha = pd.concat([df_fecha, df_values], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/balance.csv", index=False)


# bien
def balance_ccaa():
    df_final = pd.DataFrame()
    for k, v in bb.ccaa.items():
        years = [x for x in range(2013,2023)]

        for year in years:
            inicio = f"{year}-01-01"
            final = f"{year}-12-31"

            url = f"https://apidatos.ree.es/es/datos/balance/balance-electrico?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day&geo_limit=ccaa&geo_ids={v}"

            respuesta = requests.get(url).json()
            try:
                df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["content"][0]["attributes"]["values"]))["datetime"] 
            except:
                df_fecha = (pd.DataFrame(respuesta["included"][1]["attributes"]["content"][0]["attributes"]["values"]))["datetime"] 
            for n in range(len(respuesta["included"])):
                for numb in range(len(respuesta["included"][n]["attributes"]["content"])):
                    try:
                        tipo = respuesta["included"][n]["attributes"]["content"][numb]["type"]

                        nombre_col = [f"value_{tipo}", f"percentage_{tipo}"]

                        df_values = (pd.DataFrame(respuesta["included"][n]["attributes"]["content"][numb]["attributes"]["values"])).drop(["datetime"], axis = 1)

                        df_values.columns = nombre_col

                        df_fecha = pd.concat([df_fecha, df_values], axis = 1)
                    except:
                        pass
            
            df_fecha["ccaa"] = f"{k}"
            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv(f"../data/scrap/balance_ccaa.csv", index=False)

# bien
def demanda():
    df_final = pd.DataFrame()
    years = [x for x in range(2013,2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"
        respuesta = requests.get(url).json()
        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/demanda.csv", index=False)

# bien
def demanda_ccaa():
    df_final = pd.DataFrame()
    years = [x for x in range(2013,2023)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        lista_ccaa = []
        for k, v in bb.ccaa.items():
            url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month&geo_limit=ccaa&geo_ids={v}"
            respuesta = requests.get(url).json()
            df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))
            df2 = df.rename(columns = {"value": f"value{k}"})
            lista_ccaa.append(df2)

        lista_sin_fecha = [df_ccaa.drop(["datetime"], axis = 1) for df_ccaa in lista_ccaa]
        lista_sin_fecha.append(lista_ccaa[0]["datetime"])
        df_ccaa = pd.concat(lista_sin_fecha, axis = 1)
        df_final = pd.concat([df_final, df_ccaa], axis = 0)
        
    df_final.to_csv(f"../data/scrap/demanda_ccaa.csv", index=False)

#bien
def demanda_max_diaria():
    df_final = pd.DataFrame()
    years = [x for x in range(2013,2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month"
        respuesta = requests.get(url).json()

        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/demanda_max_diaria.csv", index=False)

#bien
def demanda_max_horaria():
    df_final = pd.DataFrame()
    years = [x for x in range(2013,2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month"
        respuesta = requests.get(url).json()

        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/demanda_max_horaria.csv", index=False)

#bien
def perdidas_transporte():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)] # Tienen datos desde el 2014
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/perdidas-transporte?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"
        respuesta = requests.get(url).json()

        df = pd.DataFrame(respuesta["included"][0]["attributes"]["values"])

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/perdidas_transporte.csv", index=False)

#bien
def potencia_maxima_instantanea():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/potencia-maxima-instantanea?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month"
        respuesta = requests.get(url).json()

        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/potencia_maxima_instantanea.csv", index=False)

# bien
def demanda_tiempo_real():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f'https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=hour'

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/demanda_tiempo_real.csv", index=False)

#bien
def evolucion_renovable():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f'https://apidatos.ree.es/es/datos/generacion/evolucion-renovable-no-renovable?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day'

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/evolucion_renovable_no_renovable.csv", index=False)

#bien
def evolucion_renovable_ccaa():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2023)]
    for k, v in bb.ccaa.items():
        for year in years:
            inicio = f"{year}-01-01"
            final = f"{year}-12-31"

            url = f'https://apidatos.ree.es/es/datos/generacion/evolucion-renovable-no-renovable?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month&geo_limit=ccaa&geo_ids={v}'

            respuesta = requests.get(url).json()
            try:
                df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]
            except:
                df_fecha = (pd.DataFrame(respuesta["included"][1]["attributes"]["values"]))["datetime"]
            for n in range(len(respuesta["included"])):
                try:
                    tipo = respuesta["included"][n]["type"]

                    df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                    df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                    df_fecha = pd.concat([df_fecha, df_valores], axis = 1)
                except:
                    pass
            df_fecha["ccaa"] = f"{k}"
            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/evolucion_renovable_no_renovable_ccaa.csv", index=False)

# bien (tiene ccaa, pero me parece raro este dato)
def estructura_renovable():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f'https://apidatos.ree.es/es/datos/generacion/estructura-renovables?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day'

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/estructura_renovables.csv", index=False)

# bien, se puede por ccaa
def emisiones_CO2():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f'https://apidatos.ree.es/es/datos/generacion/no-renovables-detalle-emisiones-CO2?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day'

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/emisiones_CO2.csv", index=False)


def precios_mercados():
    df_final = pd.DataFrame()
    years = [x for x in range(2014,2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f"https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=hour"
            respuesta = requests.get(url).json()

            df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"])).drop(["percentage"], axis = 1)

            df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/precios_mercados.csv", index=False)


######## Visualizacion

def px_demanda(año):
    with open(f'../data/visualizacion/px_demanda.pkl', 'rb') as demanda:
        df = pickle.load(demanda)

    df_year = df[df["Fecha"].dt.year == int(año)]
    mean_value = df_year['Demanda en MW'].mean()

    fig = px.line(df_year, x = "Fecha", y = "Demanda en MW", line_group = None)
    
    fig.add_shape(go.layout.Shape(
        type = "line",
        x0 = df_year['Fecha'].iloc[0],
        y0 = mean_value,
        x1 = df_year['Fecha'].iloc[-1],
        y1 = mean_value,
        line = dict(color = "#00072D", width = 2, dash = "dot")))

    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_demanda_real(año, semana):
    with open(f'../data/visualizacion/px_demanda_real.pkl', 'rb') as demanda_real:
        df = pickle.load(demanda_real)

    df_year2 = df[df["Fecha"].dt.year == int(año)]
    df_week2 = df_year2[df_year2["Fecha"].dt.isocalendar().week == int(semana)]
    mean_value = df_week2["Demanda real en MW"].mean()
    fig = px.line(
                df_week2,
                x='Fecha',
                y=["Demanda real en MW", "Demanda programada en MW", "Demanda prevista en MW"],
                color_discrete_sequence=['blue', 'red', "green"])
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df_week2['Fecha'].iloc[0],
            y0 = mean_value,
            x1 = df_week2['Fecha'].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
     
    fig.show()


def px_demanda_estacion():
    with open(f'../data/visualizacion/px_demanda_estacion.pkl', 'rb') as demanda_estacion:
        df = pickle.load(demanda_estacion)
    mean_value = df['Verano'].mean()
    fig = px.line(
            df,
            x='Día',
            y = ["Primavera", "Verano", "Otoño", "Invierno"],
            color_discrete_map = {"Primavera":"green", 'Verano':'red', "Otoño":"orange", "Invierno":"royalblue"})
    fig.update_layout(
        xaxis=dict(
            tickvals=[87+ (144*n) for n in range(0,7)],
            ticktext=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]),
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df['Día'].iloc[0],
            y0 = mean_value,
            x1 = df['Día'].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.show()


def px_precio_historico():
    with open(f'../data/visualizacion/px_precio_historico.pkl', 'rb') as precios_historico:
        df = pickle.load(precios_historico)
    fig = px.line(df, x = "Fecha", y = "Precio mayorista en €/MWh", line_group = None)

    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_precio_diario(año):
    with open(f'../data/visualizacion/px_precio_diario.pkl', 'rb') as precio_diario:
        df = pickle.load(precio_diario)
    
    df_year = df[df["Fecha"].dt.year == int(año)]
    mean_value = df_year['Precio mayorista en €/MWh'].mean()
    fig = px.line(df_year, x = "Fecha", y = "Precio mayorista en €/MWh", line_group = None)
    
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df_year['Fecha'].iloc[0],
            y0 = mean_value,
            x1 = df_year['Fecha'].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_porcentage_renovables_barplot():
    with open(f'../data/visualizacion/px_porcentage_renovables.pkl', 'rb') as porcentage_renovables:
        df = pickle.load(porcentage_renovables)

    fig = px.bar(
        df,
        x = 'Energia',
        y = 'Porcentage',
        color = "Tipo",
        color_discrete_map = {"Renovable": "#44CF6C", 'No Renovable': '#0E7C7B'})

    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_porcentage_renovables_sunburst():
    with open(f'../data/visualizacion/px_porcentage_renovables.pkl', 'rb') as porcentage_renovables:
        df = pickle.load(porcentage_renovables)

    fig = px.sunburst(
        df,
        path = ["Tipo", "Energia"],
        values = "Porcentage",
        color = "Tipo",
        color_discrete_map = {"Renovable": "#44CF6C", 'No Renovable': '#0E7C7B'})
    
    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))

    fig.show()


def px_balance_renovables(energias):
    with open(f'../data/visualizacion/px_balance_renovables.pkl', 'rb') as balance_renovables:
        df = pickle.load(balance_renovables)
    fig = px.line(
        df,
        x = 'Fecha',
        y = energias,
        color_discrete_map = {
        "Turbinación bombeo": "blue", "Nuclear": "green", "Ciclo combinado": "brown",
        "Carbón": "black", "Turbina de gas": "orange", "Motores diésel": "gold", "Turbina de vapor": "cyan",
        "Fuel + Gas": "pink", "Cogeneración": "grey", "Residuos no renovables": "purple", "Hidráulica": "royalblue",
        "Eólica": "lightblue", "Solar fotovoltaica": "yellow", "Solar térmica": "red", "Otras renovables": "violet",
        "Residuos renovables": "yellowgreen", "Hidroeólica": "seashell"})
    
    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_evo_reno():
    with open(f'../data/visualizacion/px_evo_reno.pkl', 'rb') as evo_reno:
        df = pickle.load(evo_reno)
    mean_value = df["percentage_Renovable"].mean()*100

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x = df['mes_y_año'], y = (df["percentage_Renovable"]*100),
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#44CF6C'),
        stackgroup='one',
        name = "Renovable"))
    
    fig.add_trace(go.Scatter(
        x = df['mes_y_año'], y = (df["percentage_No renovable"]*100),
        hoverinfo='x+y',
        mode='lines',
        line=dict(width=0.5, color='#0E7C7B'),
        stackgroup='one',
        name = "No Renovable"))
    
    fig.add_shape(go.layout.Shape(
                type = "line",
                x0 = df['mes_y_año'].iloc[0],
                y0 = mean_value,
                x1 = df['mes_y_año'].iloc[-1],
                y1 = mean_value,
                line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        yaxis_range=(0, 100),
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))

    fig.show()


def px_emisiones():
    with open(f'../data/visualizacion/px_emisiones.pkl', 'rb') as emisiones:
        df = pickle.load(emisiones)

    fig = px.line(
        df,
        x = 'Fecha',
        y = ["Carbón", "Motores diésel", "Turbina de gas", "Turbina de vapor", "Ciclo combinado", "Cogeneración", "Residuos no renovables"])
    
    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_perdidas():
    with open(f'../data/visualizacion/px_perdidas.pkl', 'rb') as perdidas:
        df = pickle.load(perdidas)

    mean_value = df["Porcentage"].mean()

    fig = px.line(df, x = "Fecha", y = "Porcentage", line_group = None)
    
    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df['Fecha'].iloc[0],
            y0 = mean_value,
            x1 = df['Fecha'].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))
    
    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()


def px_generado():
    with open(f'../data/visualizacion/px_generado.pkl', 'rb') as generado:
        df = pickle.load(generado)
        
    mean_value = df['Generación en MW'].mean()

    fig = px.line(df, x = "Fecha", y = "Generación en MW", line_group = None)

    fig.add_shape(go.layout.Shape(
            type = "line",
            x0 = df['Fecha'].iloc[0],
            y0 = mean_value,
            x1 = df['Fecha'].iloc[-1],
            y1 = mean_value,
            line = dict(color = "#00072D", width = 2, dash = "dot")))

    fig.update_layout(
        plot_bgcolor = '#E1D5D7',
        paper_bgcolor='#F7EBEC',
        font=dict(family = 'Arial', color = '#00072D'))
    
    fig.show()