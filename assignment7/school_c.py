import sqlite3

def run_query(query, params=None):
    with sqlite3.connect("../db/school.db") as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

students = run_query("SELECT * FROM Students")
print("All Students:")
for row in students:
    print(row)

filtered = run_query("SELECT * FROM Students WHERE age = ? AND major = ?", (22, 'History'))
print("\nStudents age 22 majoring in History:")
for row in filtered:
    print(row)

courses = run_query("SELECT * FROM Courses WHERE instructor_name = ?", ('Dr. Smith',))
print("\nCourses by Dr. Smith:")
for row in courses:
    print(row)
