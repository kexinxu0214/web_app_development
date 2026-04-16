from .database import get_db_connection

class Donation:
    @staticmethod
    def create(amount, message=None, user_id=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO donation (user_id, amount, message) VALUES (?, ?, ?)",
            (user_id, amount, message)
        )
        conn.commit()
        donation_id = cursor.lastrowid
        conn.close()
        return donation_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        donations = conn.execute("SELECT * FROM donation ORDER BY created_at DESC").fetchall()
        conn.close()
        return [dict(row) for row in donations]

    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        donations = conn.execute("SELECT * FROM donation WHERE user_id = ? ORDER BY created_at DESC", (user_id,)).fetchall()
        conn.close()
        return [dict(row) for row in donations]
