from flask import json


def lecturaFichero(rutaFichero):
    
    with open(rutaFichero, "r") as file:
        peliculas=json.load(file)
    
    return peliculas



def escribeFichero(rutaFichero,peliculas):
    
    with open(rutaFichero, "w") as file:
        #espera la lista y luego la ruta
        json.dump(peliculas, file)



