from flask import Flask
from flask_restx import Api
from extensions import mysql

def create_app():
    app = Flask(__name__)
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'student_user'
    app.config['MYSQL_PASSWORD'] = 'DefinedCode'
    app.config['MYSQL_DB'] = 'student_db'

    mysql.init_app(app)

    api = Api(app, doc='/swagger', title='Student API', description='API for student operations')

    # Import the namespaces after initializing the Api object to avoid circular imports
    from Services.create_student import api as create_student_ns
    from Services.get_all_students import api as get_all_students_ns
    from Services.delete_student import api as delete_student_ns
    from Services.update_student import api as update_ns
    # from .get_student_by_email import api as get_by_email_ns

    api.add_namespace(create_student_ns, path='/students')
    api.add_namespace(get_all_students_ns, path='/students')
    api.add_namespace(delete_student_ns, path='/students')
    api.add_namespace(update_ns, path='/students')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
