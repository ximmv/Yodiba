import sqlite3

conn = sqlite3.connect("yodiba.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT,
    username TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    role TEXT,
    text TEXT
)
""")

conn.commit()


def add_user(user_id, full_name, username):
    cursor.execute(
        """
        INSERT OR IGNORE INTO users (user_id, full_name, username)
        VALUES (?, ?, ?)
        """,
        (user_id, full_name, username),
    )
    conn.commit()


def save_message(user_id, role, text):
    cursor.execute(
        """
        INSERT INTO messages (user_id, role, text)
        VALUES (?, ?, ?)
        """,
        (user_id, role, text),
    )
    conn.commit()


def get_history(user_id, limit=20):
    cursor.execute(
        """
        SELECT role, text
        FROM messages
        WHERE user_id = ?
        ORDER BY id DESC
        LIMIT ?
        """,
        (user_id, limit),
    )

    rows = cursor.fetchall()
    rows.reverse()

    history = []

    for role, text in rows:
        history.append(
            {
                "role": role,
                "text": text,
            }
        )

    return history


def clear_history(user_id):
    cursor.execute(
        """
        DELETE FROM messages
        WHERE user_id = ?
        """,
        (user_id,),
    )
    conn.commit()