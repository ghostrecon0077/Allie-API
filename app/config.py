# app/config.py

from dotenv import load_dotenv
import os

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
REFERER_HEADER = "https://yourserver.com"
TITLE_HEADER = "Allie Protocol AI"
DATABASE_URL = "app/database.db"
