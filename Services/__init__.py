# Services/__init__.py
from flask import Blueprint

services_bp = Blueprint('services', __name__)

# Import all route modules to register routes with the blueprint
from . import create_student
from . import get_student_by_email
from . import update_student
from . import get_all_students
# from . import get_student_by_id
# from . import delete_student
