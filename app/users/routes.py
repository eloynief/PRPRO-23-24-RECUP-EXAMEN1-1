from flask import Blueprint,request

from utils.functions import *

from bcrypt  import *

usersBP = Blueprint("users",__name__)

rutaUsers="ficheros/users.json"

listaUsers=lecturaFichero(rutaUsers)

@usersBP.post('/')
def create_user():

    
    if request.is_json:
        #obtenemos el json que hemos cogido
        user= request.get_json()
        
        contrasena=user
        
        sal=gensalt()
        
        hashPassword = hashpw(password=contrasena, salt=sal)
            
        user["password"]=hashPassword
        
        listaUsers.append(user)
        
        escribeFichero(rutaUsers,listaUsers)
        
        return {'token':hashPassword},201
    
    return {"error":"Request must be JSON"}, 415