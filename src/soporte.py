import calendar
import pandas as pd
import requests

import sys
sys.path.append("../")
import src.biblioteca as bb

def balance():
    """
    Descarga datos de balance eléctrico de la API de apidatos.ree.es, procesa los datos y los guarda en un archivo CSV.

    Returns:
    None

    Example:
    >>> balance()
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2013, 2024)]

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

    df_final.to_csv("../data/scrap/balance.csv", index = False)


def balance_ccaa():
    """
    Obtiene los datos del balance eléctrico de diferentes comunidades autónomas de España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    for k, v in bb.ccaa.items():
        years = [x for x in range(2013, 2023)]

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

    df_final.to_csv(f"../data/scrap/balance_ccaa.csv", index = False)


def demanda():
    """
    Obtiene los datos de evolución de la demanda eléctrica en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2013, 2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"
        respuesta = requests.get(url).json()
        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/demanda.csv", index = False)


def demanda_ccaa():
    """
    Obtiene los datos de evolución de la demanda eléctrica por Comunidades Autónomas en España
    desde la API de REE, y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2013, 2023)]
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
        
    df_final.to_csv(f"../data/scrap/demanda_ccaa.csv", index = False)


def demanda_max_diaria():
    """
    Obtiene los datos de la demanda eléctrica máxima diaria en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2013, 2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month"
        respuesta = requests.get(url).json()

        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/demanda_max_diaria.csv", index = False)


def demanda_max_horaria():
    """
    Obtiene los datos de la demanda eléctrica máxima horaria en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2013, 2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/evolucion?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month"
        respuesta = requests.get(url).json()

        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/demanda_max_horaria.csv", index = False)


def perdidas_transporte():
    """
    Obtiene los datos de pérdidas en el transporte de energía eléctrica en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returs:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)] # Tienen datos desde el 2014
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/perdidas-transporte?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"
        respuesta = requests.get(url).json()

        df = pd.DataFrame(respuesta["included"][0]["attributes"]["values"])

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/perdidas_transporte.csv", index = False)


def potencia_maxima_instantanea():
    """
    Obtiene los datos de potencia máxima instantánea de demanda eléctrica en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)]
    for year in years:
        inicio = f"{year}-01-01"
        final = f"{year}-12-31"
        if year == 2023:
            final = f"{year}-03-31"
        url = f"https://apidatos.ree.es/es/datos/demanda/potencia-maxima-instantanea?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month"
        respuesta = requests.get(url).json()

        df = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]).drop(["percentage"], axis = 1))

        df_final = pd.concat([df_final, df], axis = 0)

    df_final.to_csv("../data/scrap/potencia_maxima_instantanea.csv", index = False)


def demanda_tiempo_real():
    """
    Obtiene los datos de demanda eléctrica en tiempo real en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f"https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=hour"

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/demanda_tiempo_real.csv", index = False)


def evolucion_renovable():
    """
    Obtiene los datos de evolución de la generación renovable y no renovable en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f"https://apidatos.ree.es/es/datos/generacion/evolucion-renovable-no-renovable?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/evolucion_renovable_no_renovable.csv", index = False)


def evolucion_renovable_ccaa():
    """
    Obtiene los datos de evolución de la generación renovable y no renovable por Comunidad Autónoma en España desde
    la API de REE, y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2023)]
    for k, v in bb.ccaa.items():
        for year in years:
            inicio = f"{year}-01-01"
            final = f"{year}-12-31"

            url = f"https://apidatos.ree.es/es/datos/generacion/evolucion-renovable-no-renovable?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=month&geo_limit=ccaa&geo_ids={v}"

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

    df_final.to_csv("../data/scrap/evolucion_renovable_no_renovable_ccaa.csv", index = False)


def estructura_renovable():
    """
    Obtiene los datos de estructura de generación renovable por día en España desde la API de REE, y almacena los
    datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f"https://apidatos.ree.es/es/datos/generacion/estructura-renovables?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/estructura_renovables.csv", index = False)


def emisiones_CO2():
    """
    Obtiene los datos de emisiones de CO2 por generación no renovable por día en España desde la API de REE, y
    almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)]

    for year in years:
        n_months = 13
        if year == 2023:
            n_months = 4
        days_in_months = tuple(zip([str(numero).zfill(2) for numero in range(1, n_months)], [calendar.monthrange(year, month)[1] for month in range(1, n_months)]))
        
        for month in days_in_months:
            inicio = f"{year}-{month[0]}-01"
            final = f"{year}-{month[0]}-{month[1]}"

            url = f"https://apidatos.ree.es/es/datos/generacion/no-renovables-detalle-emisiones-CO2?start_date={inicio}T00:00&end_date={final}T23:59&time_trunc=day"

            respuesta = requests.get(url).json()

            df_fecha = (pd.DataFrame(respuesta["included"][0]["attributes"]["values"]))["datetime"]

            for n in range(len(respuesta["included"])):
                tipo = respuesta["included"][n]["type"]

                df_valores = (pd.DataFrame(respuesta["included"][n]["attributes"]["values"])).drop(["datetime"], axis = 1)
                df_valores.columns = [f"value_{tipo}", f"percentage_{tipo}"]

                df_fecha = pd.concat([df_fecha, df_valores], axis = 1)

            df_final = pd.concat([df_final, df_fecha], axis = 0)

    df_final.to_csv("../data/scrap/emisiones_CO2.csv", index = False)


def precios_mercados():
    """
    Obtiene los datos de precios de mercados en tiempo real por hora en España desde la API de REE,
    y almacena los datos en un archivo CSV.

    Args:
        None

    Returns:
        None
    """
    df_final = pd.DataFrame()
    years = [x for x in range(2014, 2024)]

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

    df_final.to_csv("../data/scrap/precios_mercados.csv", index = False)