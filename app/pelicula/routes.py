from flask import Blueprint,jsonify,json,request
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
    
   
@peliculasBP.get('/<int:idPelicula>/actores')
def get_actores(idPelicula):
    
    actores=lecturaFichero(rutaActores)
    
    #por cada elemento json de los elementos jsonde la tabla
    for actor in actores:
        
        if actor["id"]==idPelicula:
            
            return actor,200
    
    
    return {"error":"Pelicula not found"},404
    
    


@peliculasBP.put('/<int:id>')
def put_peliculas(id):
    if request.is_json:
        
        data=request.get_json()
        
        peliculas=lecturaFichero(rutaPeliculas)
        
        #por cada elemento json de los elementos jsonde la tabla
        for pelicula in peliculas:
            
            if pelicula["id"]==id:
                
                
                #se modifican los elementos
                for elementoPelicula in data:
                    
                    pelicula[elementoPelicula]=data[elementoPelicula]
                    
                escribeFichero(rutaPeliculas,pelicula)
                    
                return pelicula,200
            
        data["id"]=id
        peliculas.append(data)
        escribeFichero(rutaPeliculas,pelicula)
                
    
    
    return {"error":"Pelicula not found"},404
    


@peliculasBP.delete('/<int:id>')
def delete_peliculas(id):
    
    if request.is_json:
        
        data=request.get_json()
        
        peliculas=escribeFichero(rutaPeliculas)
        
        #por cada elemento json de los elementos jsonde la tabla
        for pelicula in peliculas:
            
            if pelicula["id"]==id:
                
                
                #se modifican los elementos
                for elementoPelicula in pelicula:
                    
                    pelicula[elementoPelicula]=data[elementoPelicula]
                
                
                return pelicula,200
    
    
    return {"error":"Pelicula not found"},404


