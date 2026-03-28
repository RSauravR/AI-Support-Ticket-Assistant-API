from fastapi import APIRouter
from app.schemas.ticket_schema import TicketCreate
from app.services.ticket_service import create_ticket, get_all_tickets

router = APIRouter()

@router.post("/tickets")
def add_ticket(ticket: TicketCreate):
    return create_ticket(ticket)

@router.get("/tickets")
def fetch_tickets():
    return get_all_tickets()