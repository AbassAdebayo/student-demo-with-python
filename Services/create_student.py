from flask import request, jsonify
from flask_restx import Resource, Namespace, fields
from Models.student import Student
from app import mysql
import logging

api = Namespace('students', description='Student operations')

student_model = api.model('Student', {
    'name': fields.String(required=True, description='The student name'),
    'email': fields.String(required=True, description='The student email'),
    'age': fields.Integer(required=True, description='The student age')
})

@api.route('/')
class CreateStudent(Resource):
    @api.expect(student_model)
    @api.response(200, 'Student created successfully')
    @api.response(400, 'Email already exists')
    def post(self):
        """Create a new student"""
        data = request.json
        logging.info(f"Received data: {data}")
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM students WHERE email = %s", (data['email'],))
            existing_student = cursor.fetchone()

            if existing_student:
                return {"error": "Email already exists!"}, 400

            cursor.execute("INSERT INTO students (name, email, age) VALUES (%s, %s, %s)",
                           (data['name'], data['email'], data['age']))
            mysql.connection.commit()
            student_id = cursor.lastrowid
            cursor.close()
            new_student = Student(student_id, data['name'], data['email'], data['age'])
            logging.info(f"Created student: {new_student.to_dict()}")
            return {"message": "Student created successfully", "student": new_student.to_dict()}, 200
        except Exception as e:
            logging.error(f"Error creating student: {e}")
            return {"error": str(e)}, 500
