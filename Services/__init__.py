# Services/__init__.py
from flask import Blueprint

services_bp = Blueprint('services', __name__)

# Import all route modules to register routes with the blueprint
from . import create_student
# from . import get_students
# from . import get_student
# from . import update_student
# from . import delete_student
