from .database import get_db_connection

class Lot:
    @staticmethod
    def create(number, name, poem, explanation):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO lot (number, name, poem, explanation) VALUES (?, ?, ?, ?)",
            (number, name, poem, explanation)
        )
        conn.commit()
        lot_id = cursor.lastrowid
        conn.close()
        return lot_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        lots = conn.execute("SELECT * FROM lot").fetchall()
        conn.close()
        return [dict(row) for row in lots]

    @staticmethod
    def get_by_id(lot_id):
        conn = get_db_connection()
        lot = conn.execute("SELECT * FROM lot WHERE id = ?", (lot_id,)).fetchone()
        conn.close()
        return dict(lot) if lot else None

    @staticmethod
    def update(lot_id, number, name, poem, explanation):
        conn = get_db_connection()
        conn.execute(
            "UPDATE lot SET number = ?, name = ?, poem = ?, explanation = ? WHERE id = ?",
            (number, name, poem, explanation, lot_id)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def delete(lot_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM lot WHERE id = ?", (lot_id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def get_random():
        conn = get_db_connection()
        lot = conn.execute("SELECT * FROM lot ORDER BY RANDOM() LIMIT 1").fetchone()
        conn.close()
        return dict(lot) if lot else None
