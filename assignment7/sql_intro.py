import sqlite3

# --- TASK 2 - DATABASE SETUP ---

def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        title TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """)

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


# --- TASK 3 - INSERT FUNCTIONS ---

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, title, publisher_name):
    cursor.execute("SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
    result = cursor.fetchone()
    if result:
        publisher_id = result[0]
        try:
            cursor.execute("INSERT INTO magazines (title, publisher_id) VALUES (?, ?)", (title, publisher_id))
        except sqlite3.IntegrityError:
            print(f"Magazine '{title}' already exists.")
    else:
        print(f"Publisher '{publisher_name}' not found.")

def add_subscriber(cursor, name, address):
    cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
    if cursor.fetchone():
        print(f"Subscriber '{name}' at '{address}' already exists.")
    else:
        cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))

def add_subscription(cursor, subscriber_name, address, magazine_title, expiration_date):
    cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?", (subscriber_name, address))
    subscriber = cursor.fetchone()
    if not subscriber:
        print(f"Subscriber '{subscriber_name}' not found.")
        return
    subscriber_id = subscriber[0]

    cursor.execute("SELECT magazine_id FROM magazines WHERE title = ?", (magazine_title,))
    magazine = cursor.fetchone()
    if not magazine:
        print(f"Magazine '{magazine_title}' not found.")
        return
    magazine_id = magazine[0]

    cursor.execute("SELECT * FROM subscriptions WHERE subscriber_id = ? AND magazine_id = ?", (subscriber_id, magazine_id))
    if cursor.fetchone():
        print(f"{subscriber_name} is already subscribed to {magazine_title}.")
        return

    cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))


try:
    conn = sqlite3.connect("../db/magazines.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    create_tables(cursor)

    add_publisher(cursor, "NatGeo Media")
    add_publisher(cursor, "Condé Nast")
    add_publisher(cursor, "Time Inc")

    add_magazine(cursor, "National Geographic", "NatGeo Media")
    add_magazine(cursor, "The New Yorker", "Condé Nast")
    add_magazine(cursor, "Time Magazine", "Time Inc")

    add_subscriber(cursor, "Alice Smith", "123 Broadway, New York, NY")
    add_subscriber(cursor, "Bob Jones", "456 Park Ave, New York, NY")
    add_subscriber(cursor, "Alice Smith", "789 Fifth Ave, New York, NY")

    add_subscription(cursor, "Alice Smith", "123 Broadway, New York, NY", "National Geographic", "2025-12-31")
    add_subscription(cursor, "Bob Jones", "456 Park Ave, New York, NY", "Time Magazine", "2025-10-01")
    add_subscription(cursor, "Alice Smith", "789 Fifth Ave, New York, NY", "The New Yorker", "2026-01-15")

    conn.commit()
    print("Data inserted successfully.")

    # --- TASK 4 - SQL QUERIES ---

    print("\nAll subscribers:")
    cursor.execute("SELECT * FROM subscribers")
    for row in cursor.fetchall():
        print(row)

    print("\nAll magazines ordered alphabetically:")
    cursor.execute("SELECT * FROM magazines ORDER BY title")
    for row in cursor.fetchall():
        print(row)

    print("\nMagazines from 'NatGeo Media':")
    cursor.execute("""
        SELECT m.magazine_id, m.title, p.name AS publisher_name
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.publisher_id
        WHERE p.name = ?
    """, ("NatGeo Media",))
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()
        print("Connection closed.")