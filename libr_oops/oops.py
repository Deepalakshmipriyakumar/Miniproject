import mysql.connector

class Student:
    def __init__(self, name, course, marks):
        self.name = name
        self.course = course
        self.marks = marks

class DatabaseManager:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Deepa@2000",
            database="oop"
        )

    def execute(self, query, params=()):
        cursor = self.conn.cursor(buffered=True)  # Use a new cursor for every query
        cursor.execute(query, params)
        self.conn.commit()
        return cursor

class StudentManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_student(self, student):
        query = "INSERT INTO lib_oop (name, course, marks) VALUES (%s, %s, %s)"
        self.db.execute(query, (student.name, student.course, student.marks))
        print("Student added successfully")

    def view_all_students(self):
        query = "SELECT * FROM lib_oop"
        cursor = self.db.execute(query)
        rows = cursor.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Course: {row[2]}, Marks: {row[3]}")
        else:
            print("No students found in database")

    def update_student(self, student_id, name, course, marks):
        query = "UPDATE lib_oop SET name=%s, course=%s, marks=%s WHERE id=%s"
        self.db.execute(query, (name, course, marks, student_id))
        print("Student updated successfully")

    def delete_student(self, student_id):
        query = "DELETE FROM lib_oop WHERE id=%s"
        self.db.execute(query, (student_id,))
        print("Student deleted successfully")

    def search_student(self, student_id):
        query = "SELECT * FROM lib_oop WHERE id=%s"
        cursor = self.db.execute(query, (student_id,))
        result = cursor.fetchone()
        if result:
            print(f"ID: {result[0]}, Name: {result[1]}, Course: {result[2]}, Marks: {result[3]}")
        else:
            print("Student not found")

def menu():
    sm = StudentManager()
    while True:
        print("\n-- Student Record Management (MySQL) --")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student by ID")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            course = input("Enter the course: ")
            marks = int(input("Enter the marks: "))
            sm.add_student(Student(name, course, marks))
        elif choice == "2":
            sm.view_all_students()
        elif choice == "3":
            student_id = int(input("Enter the student ID: "))
            name = input("Enter the new name: ")
            course = input("Enter the new course: ")
            marks = int(input("Enter the new marks: "))
            sm.update_student(student_id, name, course, marks)
        elif choice == "4":
            student_id = int(input("Enter the student ID: "))
            sm.delete_student(student_id)
        elif choice == "5":
            student_id = int(input("Enter the student ID: "))
            sm.search_student(student_id)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
