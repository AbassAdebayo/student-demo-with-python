from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import Config
from Services import services_bp
from flasgger import Swagger
from flask_swagger_ui import get_swaggerui_blueprint
import logging

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

swagger = Swagger(app)

# Register the blueprint
app.register_blueprint(services_bp)


# Setup Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/create_student.yml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "Student API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
