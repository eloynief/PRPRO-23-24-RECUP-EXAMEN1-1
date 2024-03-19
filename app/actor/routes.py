from flask import Blueprint,jsonify

from utils.functions import *

from actor.routes import *

#bp con su nombre
actoresBP=Blueprint("actores",__name__)


#como se ejecuta desde la carpeta anterior a app, pues se aproxima a app
rutaActores="app/ficheros/actores.json"

@actoresBP.get('/<int:id>')
def get_actor(id):
    
    
    actores=lecturaFichero(rutaActores)
    
    #por cada elemento json de los elementos jsonde la tabla
    for actor in actores:
        
        if actor["id"]==id:
            
            return actor,200
    
    
    return {"error":"Actor not found"},404


@actoresBP.post('/<int:id>')
def post_actor(id):
    
    
    actores=lecturaFichero(rutaActores)
    
    #por cada elemento json de los elementos jsonde la tabla
    for actor in actores:
        
        if actor["id"]==id:
            
            return actor,200
    
    
    return {"error":"Actor not found"},404



def aumentaTamanoLista():
    return (i["id"]for i in )+1