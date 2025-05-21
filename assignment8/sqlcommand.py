import sqlite3

conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()

while True:
    try:
        command = input("Enter a SQL command:\n")
        if command.lower() in ('exit', 'quit'):
            break
        cursor.execute(command)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Error:", e)

conn.close()
