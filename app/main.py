from fastapi import FastAPI
from app.config.db import connect_db
from app.routes import ticket_routes

app = FastAPI()

connect_db()

app.include_router(ticket_routes.router)

@app.get("/")
def root():
    return {"message": "API running with MongoDB Atlas"}