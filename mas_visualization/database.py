# database.py
from databases import Database
from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

load_dotenv()
# Define the database file
# mas_visualization/database.py
DATABASE_URL = os.getenv("DATABASE_URL","sqlite:///./mas_visualization/lab_assistant.db")

# Create the core database objects
database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL)