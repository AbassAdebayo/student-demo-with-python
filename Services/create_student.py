from flask import request, jsonify
from Services import services_bp
from Models.student import Student
from app import mysql
import logging

logging.info("Registering create_student routes")

@services_bp.route('/students', methods=['POST'])
@swag_from({
    
    'tags': ['Students'],
    'description': 'Create a new student',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'age': {'type': 'integer'}
                },
                'example': {
                    'name': 'John Doe',
                    'email': 'john.doe@example.com',
                    'age': 21
                }
            }
        }
    ],
    'responses': {
        '201': {
            'description': 'Student created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'student_id': {'type': 'integer'},
                    'name': {'type': 'string'},
                    'email': {'type': 'string'},
                    'age': {'type': 'integer'}
                },
                'example': {
                    'student_id': 1,
                    'name': 'John Doe',
                    'email': 'john.doe@example.com',
                    'age': 21
                }
            }
        },
        '500': {
            'description': 'Error creating student',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string'}
                }
            }
        }
    }
})
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
