from flask import request, jsonify
from Services import services_bp
from Models.student import Student
from app import mysql
from flasgger.utils import swag_from
import logging


@services_bp.route('/students/', methods=['GET'])
@swag_from('../static/swagger_openai.yml', endpoint='get_all_students')

def get_all_students():
    
    students = []
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, name, email, age FROM students")
        students = cursor.fetchall()
        cursor.close()
        logging.debug(f"Query executed successfully, fetched {len(students)} students")
    
        
        student_list = []
        
        for student in students:
            logging.debug(f"Processing student: {student}") 
            student_data = Student(student[0], student[1], student[2], student[3])
            student_list.append(student_data.to_dict())
        
        logging.debug("All students processed successfully")
        return jsonify(students), 200   
    except Exception as e:
        logging.error(f"Error fetching students: {e}")
        return jsonify({"message": "Error fetching students"}), 500