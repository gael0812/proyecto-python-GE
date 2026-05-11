def contar_genero(personajes):

    hombres = 0
    mujeres = 0

    for personaje in personajes:

        genero = personaje.get("genero", "")

        if genero == "Male":
            hombres += 1

        elif genero == "Female":
            mujeres += 1

    return hombres, mujeres


def grafica_genero(hombres, mujeres):

    total = hombres + mujeres

    if total == 0:
        print("No hay datos para graficar")
        return

    plt.figure()

    plt.pie(
        [hombres, mujeres],
        labels=["Hombres", "Mujeres"],
        autopct="%1.1f%%",
        colors=["skyblue", "pink"]
    )

    plt.title("Género de personajes de Los Simpson")

    plt.savefig("grafica1.png")

    plt.show()


def contar_edades(datos):

    rangos = {
        "0-10": 0,
        "11-20": 0,
        "21-30": 0,
        "31-40": 0,
        "41-50": 0,
        "51+": 0
    }

    for personaje in datos:

        edad = personaje.get("age", 0)

        try:
            edad = int(edad)
        except:
            continue

        if edad <= 10:
            rangos["0-10"] += 1
        elif edad <= 20:
            rangos["11-20"] += 1
        elif edad <= 30:
            rangos["21-30"] += 1
        elif edad <= 40:
            rangos["31-40"] += 1
        elif edad <= 50:
            rangos["41-50"] += 1
        else:
            rangos["51+"] += 1

    return rangos

def grafica_edades(rangos):

    valores = list(rangos.values())

    if sum(valores) == 0:
        print("No hay datos de edades para graficar")
        return

    plt.figure()

    plt.bar(
        rangos.keys(),
        valores,
        color="orange"
    )

    plt.title("Edades de personajes de Los Simpson")
    plt.xlabel("Rango de edad")
    plt.ylabel("Cantidad")

    plt.savefig("grafica2.png")
                
    plt.show()

