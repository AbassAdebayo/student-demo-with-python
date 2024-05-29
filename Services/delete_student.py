from flask import request
from flask_restx import Resource, Namespace, fields
from Models.student import Student
from app import mysql
import logging

api = Namespace('Delete Student')

@api.route('/<int:student_id>')
class DeleteStudent(Resource):
    @api.response(200, 'Student deleted successfully')
    @api.response(400, 'Student not found')
    def delete(self, student_id):
        """Delete a student by ID"""
        logging.info(f"Deleting a student with ID: {student_id}")
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM students WHERE id = %s", (student_id,))
            existing_student = cursor.fetchone()
            if not existing_student: return {"error": "Student not found!"}, 404
            cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
            mysql.connection.commit()
            cursor.close()
            logging.info(f"Student with ID: {student_id} deleted")
            return {"message": "Student deleted successfully"}, 200
        except Exception as e:
            logging.error(f"Error while deleting student: {e}")
            return {"error": str(e)}, 500
            

            