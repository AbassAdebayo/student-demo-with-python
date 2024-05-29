from flask import request
from flask_restx import Resource, Namespace, fields
from Models.student import Student
from app import mysql
import logging

api = Namespace('Update Student')

student_model = api.model('Student', {
    'name': fields.String(required=True, description='The student\'s name'),
    'email': fields.String(required=True, description='The student\'s email'),
    'age': fields.Integer(required=True, description='The student\'s age')
})

@api.route('/<int:student_id>')
class UpdateStudent(Resource):
    @api.expect(student_model)
    @api.response(200, 'Student updated successfully')
    @api.response(400, 'student not found')
    def put(self, student_id):
        """"Update student by ID"""
        data = request.json
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            existing_student = cursor.fetchone()

            if not existing_student:
                return {"error": "Student not found!"}, 404

            cursor.execute("UPDATE students SET name = %s, email = %s, age = %s WHERE id = %s",
                           (data['name'], data['email'], data['age'], student_id))
            mysql.connection.commit()
            cursor.close()
            updated_student = Student(student_id, data['name'], data['email'], data['age'])
            logging.info(f"Updated student: {updated_student.to_dict()}")
            return {"message": "Student updated successfully", "student": updated_student.to_dict()}, 200
        except Exception as e:
            logging.error(f"Error updating student: {e}")
            return {"error": str(e)}, 500
        

    
    
    