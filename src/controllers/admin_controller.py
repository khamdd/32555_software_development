from src.models.student import Student
from src.models.database import Database
from typing import Dict, List
from src.common.utils import Utils

class AdminController:
    def __init__(self, database: Database):
        self.database = database
        
    def clear_database(self):
        print("Clearing students database")
        confirm = input("Are you sure you want to clear the database (Y)ES/(N)O: ").lower()
        if(confirm == "y"):
            self.database.student_list = []
            self.database.write_file()
        
    def show_all_students(self):
        print("Student List")
        for student in self.database.student_list:
            print(f"{student.name} :: {student.student_id} --> Email: {student.email}")
            
    def group_students(self):
        students_sorted_by_grade = sorted(
            self.database.student_list,
            key=lambda student: sum(subject.mark for subject in student.subjects) / len(student.subjects),
            reverse=True
        )
        
        for student in students_sorted_by_grade:
            average_mark = sum(subject.mark for subject in student.subjects) / len(student.subjects)
            print(f"{Utils.grade_calculate(average_mark)} --> {student.name} :: {student.student_id} --> Email: {student.email}")