from mongoengine import connect
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    connect(
        db="ticket_db",
        host=os.getenv("MONGO_URI")
    )