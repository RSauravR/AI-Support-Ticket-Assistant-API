from fastapi import APIRouter
from app.schemas.ticket_schema import TicketCreate
from app.services.ticket_service import create_ticket, get_all_tickets, update_ticket, delete_ticket
from typing import Optional

router = APIRouter()

@router.post("/tickets")
def add_ticket(ticket: TicketCreate):
    return create_ticket(ticket)

@router.get("/tickets")
def fetch_tickets(priority: Optional[str] = None):
    return get_all_tickets(priority)

@router.put("/tickets/{ticket_id}")
def edit_ticket(ticket_id: str, ticket: TicketCreate):
    return update_ticket(ticket_id, ticket)

@router.delete("/tickets/{ticket_id}")
def remove_ticket(ticket_id: str):
    return delete_ticket(ticket_id)