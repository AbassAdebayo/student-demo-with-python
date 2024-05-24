# config.py
import os

class Config:
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'student_user')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'DefinedCode')
    MYSQL_DB = os.getenv('MYSQL_DB', 'student_db')
    MYSQL_CURSORCLASS = 'DictCursor'
