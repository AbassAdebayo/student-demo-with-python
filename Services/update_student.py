from flask import request, jsonify
from Services import services_bp
from Models.student import Student
from app import mysql
from flasgger.utils import swag_from
import logging


@services_bp.route('/students/<int:student_id>', methods=['PUT'])
@swag_from('../static/swagger_openai.yml', endpoint='update_student')

def update_student(student_id):
    data  = request.json
    cursor = mysql.connection.cursor()
    
    try:
        cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        existing_student = cursor.fetchone()
    
        if not existing_student:
            return jsonify({"message": "Student not found"}), 404
        cursor.execute("UPDATE students SET name = %s, age= %s, email = %s WHERE id = %s", 
                   (data['name'], data['age'], data['email'], student_id))
        mysql.connection.commit()
        cursor.close()
        updated_student = Student(student_id, data['name'], data['email'], data['age'])
    
        return jsonify({"message": f"Student {data['name']} updated successfully", "student": updated_student.to_dict()}), 200
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({"message": f"Error while updating Student: {str(e)}"})
    finally:
        cursor.close()

    
    
    