from flask import Blueprint,jsonify,json
from utils.functions import *

from actor.routes import *

#bp con su nombre
peliculasBP=Blueprint('peliculas',__name__)

#como se ejecuta desde la carpeta anterior a app, pues se aproxima a app
rutaPeliculas="app/ficheros/peliculas.json"



@peliculasBP.get('/')
def get_peliculas():
    peliculas=lecturaFichero(rutaPeliculas)
    return jsonify(peliculas)




@peliculasBP.get('/<int:id>')
def get_pelicula(id):
    
    
    peliculas=lecturaFichero(rutaPeliculas)
    
    #por cada elemento json de los elementos jsonde la tabla
    for pelicula in peliculas:
        
        if pelicula["id"]==id:
            
            return pelicula,200
    
    
    return {"error":"Pelicula not found"},404
    
   
@peliculasBP.get('/<int:id>/actores')
def get_actores(id):
    #lista para añadir los 
    lista=[]
    
    peliculas=lecturaFichero(rutaActores)
    
    #por cada elemento json de los elementos jsonde la tabla
    for pelicula in peliculas:
        
        if pelicula["id"]==id:
            
            return pelicula,200
    
    
    return {"error":"Pelicula not found"},404
    
    
    






