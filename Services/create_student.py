from flask import request, jsonify
from Services import services_bp
from Models.student import Student
from app import mysql
import logging

logging.info("Registering create_student routes")

@services_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    logging.info(f"Received data: {data}")
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO students (name, email, age) VALUES (%s, %s, %s)", (data['name'], data['email'], data['age']))
        mysql.connection.commit()
        student_id = cursor.lastrowid
        cursor.close()
        new_student = Student(student_id, data['name'], data['email'], data['age'])
        logging.info(f"Created student: {new_student.to_dict()}")
        return jsonify(new_student.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating student: {e}")
        return jsonify({"error": str(e)}), 500
