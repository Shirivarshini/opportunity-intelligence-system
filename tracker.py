from database import connect

def add_application(company, role, status, date, link):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO applications (company, role, status, date, link)
    VALUES (?, ?, ?, ?, ?)
    """, (company, role, status, date, link))

    conn.commit()
    conn.close()


def view_applications():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applications")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()


def update_status(app_id, new_status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE applications
    SET status = ?
    WHERE id = ?
    """, (new_status, app_id))

    conn.commit()
    conn.close()