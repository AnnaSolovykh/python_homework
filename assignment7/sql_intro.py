# TASK 1
import sqlite3

# try:
#     conn = sqlite3.connect("../db/magazines.db")
#     print("Connection opened")
# except sqlite3.Error as e:
#     print(f"Error occurred: {e}")
# finally:
#     if conn:
#         conn.close()
#         print("Connection closed")

# TASK 2
try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # publishers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )    
    """)

    # magazines
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)  
    )    
    """)

    # subscribers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )    
    """)

    # subscriptions
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
    )    
    """)

    print("All tables created successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Connection closed.")
