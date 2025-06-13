# app/memory.py

from app.database import get_db_connection
from app.models import initialize_database

# 📦 Initialize DB schema on import
initialize_database()

# ⏪ Get context for the last 6 messages (3 exchanges)
def get_context_for_user(user_id: str, limit: int = 6):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT role, message FROM memory
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT ?
        """,
        (user_id, limit)
    )
    rows = cursor.fetchall()
    conn.close()

    # Reverse to maintain chronological order
    return [{"role": row["role"], "content": row["message"]} for row in reversed(rows)]

# 💾 Save new message to memory
def save_message_to_memory(user_id: str, message: str, role: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO memory (user_id, role, message)
        VALUES (?, ?, ?)
        """,
        (user_id, role, message)
    )
    conn.commit()
    conn.close()
