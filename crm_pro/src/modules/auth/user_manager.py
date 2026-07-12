from database import connect
from modules.auth.password_manager import hash_password
from database import add_user


def create_default_admin():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=?",
        ("admin",)
    )

    user = cursor.fetchone()

    if user:
        conn.close()
        return

    password = hash_password("admin123")

    cursor.execute(
        """
        INSERT INTO users
        (
            username,
            password_hash,
            full_name,
            role,
            status
        )
        VALUES (?,?,?,?,?)
        """,
        (
            "admin",
            password,
            "System Administrator",
            "Admin",
            "Active"
        )
    )

    conn.commit()
    conn.close()


def get_user(username):

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            username,
            password_hash,
            role,
            status
        FROM users
        WHERE username=?
        """,
        (username,)
    )

    user = cursor.fetchone()

    conn.close()

    return user

def create_user(
    username,
    password,
    full_name,
    role,
    status
):
    existing_user = get_user(username)

    if existing_user:
        return False
    password_hash = hash_password(password)

    add_user(
        username,
        password_hash,
        full_name,
        role,
        status
    )
    return True