def limpiar_datos(datos):
    datos_limpios = []

    for personaje in datos:
        personaje_limpio = {
            "nombre": personaje.get("name", "sin nombre"),
            "age": personaje.get("age", "desconocida"),
            "genero": personaje.get("gender", "Desconocido"),
            "ocupacion": personaje.get("occupation", "Desconocida"),
            "imagen": personaje.get("portrait_path", None)
            }
        if personaje_limpio["nombre"]:
            datos_limpios.append(personaje_limpio)

    return datos_limpios

