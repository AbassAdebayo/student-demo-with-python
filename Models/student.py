class Student:
    def __init__(student, student_id, name, email, age):
        student.student_id = student_id
        student.name = name
        student.email = email
        student.age = age
        
        
              
def to_dict(student):
    return{
        'student_id': student.student_id,
        'name': student.name,
        'email': student.email,
        'age': student.age
    }
    
