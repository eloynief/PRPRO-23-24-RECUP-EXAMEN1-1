import json


def lecturaFichero(rutaFichero):
    try:
        with open(rutaFichero, "r") as file:
            datos=json.load(file)
        
    except json.JSONDecodeError:
        datos=[]
        
    
    return datos



def escribeFichero(rutaFichero,datos):
    
    with open(rutaFichero, "w") as file:
        #espera la lista y luego la ruta
        json.dump(datos, file)



