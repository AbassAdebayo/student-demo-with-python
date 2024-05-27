from flask import request, jsonify
from Services import services_bp
from Models.student import Student
from app import mysql
from flasgger.utils import swag_from
import logging


@services_bp.route('/students/<email>/', methods=['GET'])
@swag_from('../static/swagger_openai.yml', endpoint='get_student_by_email')
def get_student_by_email(email):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM students WHERE email= %s", (email,))
    result = cursor.fetchone()
    cursor.close()
    
    if result:
        get_student = Student(result['id'], result['name'], result['email'], result['age'])
        logging.info(f"Created student: {get_student.to_dict()}")
        return jsonify({"message": f"Student with email: {email} retrieved successfully", "student": get_student.to_dict()}), 200
    else:
        return jsonify({"message": f"Student with email: {email} not found!"}), 404