# app/database.py

import sqlite3
from app.config import DATABASE_URL

def get_db_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn
