from flask import *
from actor.routes import actoresBP
from pelicula.routes import peliculasBP


#objeto
app = Flask(__name__)


app.register_blueprint(actoresBP, url_prefix='/actores')

app.register_blueprint(peliculasBP, url_prefix='/peliculas')

#main "function"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5696)
    