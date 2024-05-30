from flask_restx import Resource, Namespace
from Models.student import Student
from extensions import mysql
import logging

api = Namespace('Get Student By Email')

@api.route('/<string:email>')
class GetStudentByEmail(Resource):
    def get(self, email):
        """Get student by email"""
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT * FROM students WHERE email= %s", (email,))
            get_student = cursor.fetchone()
            cursor.close()
            if not get_student: return {"error": "Student not found!"}, 404
            
            fetched_student = {
                'student_id': get_student[0],
                'name': get_student[1],
                'email': get_student[2],
                'age': get_student[3]
            }
            student = Student(**fetched_student)
            logging.info(f"Retrieved student: {student.to_dict()}")
            return {"message": "Student retrieved successfully", "student": student.to_dict()}, 200
        except Exception as e:
                logging.error(f"Error retrieving deleting student: {e}")
                return {"error": str(e)}, 500
        
        