import sqlite3

def connect():
    return sqlite3.connect("apps.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT,
        role TEXT,
        status TEXT,
        date TEXT,
        link TEXT
    )
    """)

    conn.commit()
    conn.close()