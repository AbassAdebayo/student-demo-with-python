from flask import jsonify
from flask_restx import Resource, Namespace
from Models.student import Student
from extensions import mysql
import logging

api = Namespace('All Students')

@api.route('/')
class GetAllStudents(Resource):
    def get(self):
        """Get all students"""
        students = []
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("SELECT id, name, email, age FROM students")
            get_all_students = cursor.fetchall()
            cursor.close()

            for student in get_all_students:
                student_data = Student(student[0], student[1], student[2], student[3])
                students.append(student_data.to_dict())

            return students, 200
        except Exception as e:
            logging.error(f"Error fetching students: {e}")
            return {"message": "Error fetching students"}, 500
