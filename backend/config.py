from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
APP_ENV = os.getenv("APP_ENV", "development")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env")
    