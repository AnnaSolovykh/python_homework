import sqlite3

with sqlite3.connect("../db/school.db") as conn:
    cursor = conn.cursor()

    # JOIN-запрос: студент + курс
    cursor.execute("""
    SELECT Students.name, Courses.course_name
    FROM Enrollments
    JOIN Students ON Enrollments.student_id = Students.student_id
    JOIN Courses ON Enrollments.course_id = Courses.course_id
    """)

    results = cursor.fetchall()
    print("Enrollments:")
    for row in results:
        print(f"{row[0]} is enrolled in {row[1]}")
