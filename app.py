from flask import Flask
from flask_restx import Api
from extensions import mysql
from Services import services_bp

def create_app():
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'student_user'
    app.config['MYSQL_PASSWORD'] = 'DefinedCode'
    app.config['MYSQL_DB'] = 'student_db'
    
    mysql.init_app(app)
    
    api = Api(app, version='1.0', title='Student API', description='A simple Student API')
    
    # Register your blueprint
    app.register_blueprint(services_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



