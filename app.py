from flask import Flask
from flask_mysqldb import MySQL
from config import Config
from flasgger import Swagger
import logging

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

swagger = Swagger(app)

@app.route('/')
def index():
    return "Welcome to the Student API!"


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
