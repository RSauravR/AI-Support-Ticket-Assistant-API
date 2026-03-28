from app.models.ticket_model import Ticket

def create_ticket(data):
    ticket = Ticket(
        title=data.title,
        description=data.description,
        priority=data.priority
    )
    ticket.save()
    return {
        "id": str(ticket.id),  # type: ignore
        "title": ticket.title,
        "description": ticket.description,
        "priority": ticket.priority
    }

def get_all_tickets():
    tickets = Ticket.objects()  # type: ignore
    
    return [
        {
            "id": str(ticket.id),  # type: ignore
            "title": ticket.title,
            "description": ticket.description,
            "priority": ticket.priority
        }
        for ticket in tickets
    ]