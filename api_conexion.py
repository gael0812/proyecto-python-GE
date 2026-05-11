import requests

def obtener_datos():
    """Descarga y retorna los datos JSON de la API."""
    url = "https://thesimpsonsapi.com/api/characters?page=1"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos.get("results", [])

if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
