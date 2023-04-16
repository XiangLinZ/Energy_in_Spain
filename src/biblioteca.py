ccaa = {"Andalucia": 4, "Aragon": 5, "Cantabria": 6, "Castilla_la_Mancha": 7, "Castilla_y_Leon": 8, "Cataluña": 9, "Pais_Vasco": 10, "Principado_de_Asturias" : 11,
        "Comunidad_de_Ceuta": 8744, "Comunidad_de_Melilla": 8745, "Comunidad_de_Madrid": 13, "Comunidad_de_Navarra": 14, "Comunidad_Valenciana": 15, "Extremadura": 16,
        "Galicia": 17, "Islas_Baleares": 8743, "Islas_Canarias": 8742, "La_Rioja": 20, "Region_de_Murcia": 21}

balance = ["balance-electrico"]

demanda = ["evolucion", "variacion-componentes", "variacion-componentes-movil", "ire-general", "ire-general-anual", "ire-general-anual", "ire-general-movil",
        "ire-industria", "ire-industria-anual", "ire-industria-movil", "ire-servicios", "ire-servicios-anual", "ire-servicios-movil", "ire-otras", "ire-otras-anual",
        "ire-otras-movil", "demanda-maxima-diaria", "demanda-maxima-horaria", "perdidas-transporte", "potencia-maxima-instantanea", "variacion-demanda",
        "potencia-maxima-instantanea-variacion", "potencia-maxima-instantanea-variacion-historico", "demanda-tiempo-real", "variacion-componentes-anual"]

generacion = ["estructura-generacion", "evolucion-renovable-no-renovable", "estructura-renovables", "estructura-generacion-emisiones-asociadas",
        "evolucion-estructura-generacion-emisiones-asociadas", "no-renovables-detalle-emisiones-CO2", "maxima-renovable", "potencia-instalada",
        "maxima-renovable-historico", "maxima-sin-emisiones-historico"]

mecados = ["componentes-precio-energia-cierre-desglose", "componentes-precio", "energia-gestionada-servicios-ajuste", "energia-restricciones", "precios-restricciones",
        "reserva-potencia-adicional", "banda-regulacion-secundaria", "energia-precios-regulacion-secundaria", "energia-precios-regulacion-terciaria",
        "energia-precios-gestion-desvios", "coste-servicios-ajuste", "volumen-energia-servicios-ajuste-variacion", "precios-mercados-tiempo-real",
        "energia-precios-ponderados-gestion-desvios-before", "energia-precios-ponderados-gestion-desvios", "energia-precios-ponderados-gestion-desvios-after"]

tipos_energia = ["Turbinación bombeo", "Nuclear", "Ciclo combinado", "Carbón", "Turbina de gas", "Motores diésel", "Turbina de vapor", "Fuel + Gas", "Cogeneración",
        "Residuos no renovables", "Hidráulica", "Eólica", "Solar fotovoltaica", "Solar térmica", "Otras renovables", "Residuos renovables", "Hidroeólica"]

estaciones = {"Primavera": ["03-20", "06-20"],
              "Verano": ["06-21", "09-22"],
              "Otoño": ["09-22", "12-21"],
              "Invierno": ["12-22", "03-19"]}