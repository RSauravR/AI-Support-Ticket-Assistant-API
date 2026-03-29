from app.models.ticket_model import Ticket
from fastapi import HTTPException
from typing import Optional

def create_ticket(data):
    try:
        ticket = Ticket(
            title=data.title,
            description=data.description,
            priority=data.priority if data.priority else "medium"
        )
        ticket.save()
        return {
            "id": str(ticket.id),  # type: ignore
            "title": ticket.title,
            "description": ticket.description,
            "priority": ticket.priority
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_all_tickets(priority: Optional[str] = None):
    try:
        if priority:
            tickets = Ticket.objects(priority=priority)  # type: ignore
        else:
            tickets = Ticket.objects() #type: ignore
        
        return [
            {
                "id": str(ticket.id),  # type: ignore
                "title": ticket.title,
                "description": ticket.description,
                "priority": ticket.priority
            }
            for ticket in tickets
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def update_ticket(ticket_id: str, data):
    try:
        ticket = Ticket.objects(id=ticket_id).first()  # type: ignore

        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")

        ticket.title = data.title
        ticket.description = data.description

        # optional priority update
        if data.priority:
            ticket.priority = data.priority

        ticket.save()

        return {
            "id": str(ticket.id),  # type: ignore
            "title": ticket.title,
            "description": ticket.description,
            "priority": ticket.priority,
        }

    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
    
def delete_ticket(ticket_id: str):
    try:
        ticket = Ticket.objects(id=ticket_id).first()  # type: ignore

        if not ticket:
            raise HTTPException(status_code=404, detail="Ticket not found")

        ticket.delete()

        return {
            "success": True,
            "message": "Ticket deleted successfully"
        }
    
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")