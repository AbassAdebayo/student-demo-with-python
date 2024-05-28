from flask import Blueprint
from flask_restx import Api

services_bp = Blueprint('services', __name__)
api = Api(services_bp)

from .create_student import api as create_ns
# from .update_student import api as update_ns
# from .get_student_by_email import api as get_by_email_ns
# from .get_all_students import api as get_all_ns

api.add_namespace(create_ns, path='/students')
# api.add_namespace(update_ns)
# api.add_namespace(get_by_email_ns)
# api.add_namespace(get_all_ns)
