from flask import Blueprint,jsonify,request

from utils.functions import *

from actor.routes import *

from app.pelicula.routes import *

from users.routes import *


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
    
    if request.is_json:
        
        actor=json.loads(request.data)
        
        actor["id"]=aumentaTamanoLista()
        
        actores=lecturaFichero(rutaActores)
        
        actores.append(actor)
        
        with open(rutaActores, "w") as file:
            json.dump(actores, file)
        
        return actor,201
    
    return {"error":"Request debe ser json"},415



@actoresBP.delete('/<int:id>')
def delete_actor(id):
    
    if request.is_json:
        
        data=request.get_json()
        
        actores=escribeFichero(rutaActores)
        
        #por cada elemento json de los elementos jsonde la tabla
        for actor in actores:
            
            if actor["id"]==id:
                
                
                #se modifican los elementos
                for elementoActor in actor:
                    
                    actor[elementoActor]=data[elementoActor]
                
                
                return actor,200
    
    
    return {"error":"actor not found"},404





def aumentaTamanoLista():
    
    actores=lecturaFichero(rutaActores)
    
    return (i["id"]for i in actores)+1