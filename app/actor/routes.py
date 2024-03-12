from flask import Blueprint,jsonify

#bp con su nombre
actoresBP=Blueprint("actores",__name__)


#como se ejecuta desde la carpeta anterior a app, pues se aproxima a app
rutaActores="app/ficheros/actores.json"