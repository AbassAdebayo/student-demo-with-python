from flask import request, jsonify
from Services import services_bp
from Models.student import Student
from app import mysql
from flasgger.utils import swag_from
import logging

logging.info("Registering create_student routes")

@services_bp.route('/students', methods=['POST'])
@swag_from('../static/create_student.yml')             
def create_student():
    data = request.json
    logging.info(f"Received data: {data}")
    try:
        cursor = mysql.connection.cursor()
        
        # check if email exists
        cursor.execute("SELECT * FROM students WHERE email = %s", (data['email'],))
        existing_student = cursor.fetchone()
        
        if existing_student:
            return jsonify({"error": "Email already exists!"}), 400
        
        cursor.execute("INSERT INTO students (name, email, age) VALUES (%s, %s, %s)", (data['name'], data['email'], data['age']))
        mysql.connection.commit()
        student_id = cursor.lastrowid
        cursor.close()
        new_student = Student(student_id, data['name'], data['email'], data['age'])
        logging.info(f"Created student: {new_student.to_dict()}")
        return jsonify({"message": "Student created successfully", "student": new_student.to_dict()}), 200
    except Exception as e:
        logging.error(f"Error creating student: {e}")
        return jsonify({"error": str(e)}), 500
