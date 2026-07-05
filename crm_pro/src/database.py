import sqlite3

DB_NAME = "crm_pro/data/contacts.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        phone TEXT NOT NULL

    )
    """)

    conn.commit()
    conn.close()


def add_contact(name, phone):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contacts(name, phone) VALUES(?,?)",
        (name, phone)
    )

    conn.commit()
    conn.close()


def get_contacts():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM contacts")

    data = cursor.fetchall()

    conn.close()

    return data


def delete_contact(contact_id):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contacts WHERE id=?",
        (contact_id,)
    )

    conn.commit()

    conn.close()


def update_contact(contact_id, name, phone):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE contacts
        SET name=?, phone=?
        WHERE id=?
        """,
        (name, phone, contact_id)
    )

    conn.commit()

    conn.close()


def search_contact(keyword):

    conn = connect()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM contacts
        WHERE name LIKE ?
        OR phone LIKE ?
        """,
        ('%' + keyword + '%',
         '%' + keyword + '%')
    )

    data = cursor.fetchall()

    conn.close()

    return data

def get_total_contacts():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM contacts"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total

def get_today_contacts():
    return get_total_contacts()