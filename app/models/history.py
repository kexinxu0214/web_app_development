from .database import get_db_connection

class History:
    @staticmethod
    def create(user_id, lot_id, question=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO history (user_id, lot_id, question) VALUES (?, ?, ?)",
            (user_id, lot_id, question)
        )
        conn.commit()
        history_id = cursor.lastrowid
        conn.close()
        return history_id

    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        records = conn.execute("SELECT * FROM history WHERE user_id = ? ORDER BY created_at DESC", (user_id,)).fetchall()
        conn.close()
        return [dict(row) for row in records]

    @staticmethod
    def get_by_id(history_id):
        conn = get_db_connection()
        record = conn.execute("SELECT * FROM history WHERE id = ?", (history_id,)).fetchone()
        conn.close()
        return dict(record) if record else None

    @staticmethod
    def delete(history_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM history WHERE id = ?", (history_id,))
        conn.commit()
        conn.close()
