from .database import get_db_connection

class User:
    @staticmethod
    def create(username, email, password_hash):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO user (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def get_by_email(email):
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM user WHERE email = ?", (email,)).fetchone()
        conn.close()
        return dict(user) if user else None

    @staticmethod
    def update(user_id, username=None, password_hash=None):
        conn = get_db_connection()
        if username:
            conn.execute("UPDATE user SET username = ? WHERE id = ?", (username, user_id))
        if password_hash:
            conn.execute("UPDATE user SET password_hash = ? WHERE id = ?", (password_hash, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(user_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM user WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()
