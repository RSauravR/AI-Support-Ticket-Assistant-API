from typing import Optional
from app.models.ticket_model import Ticket
from fastapi import HTTPException
from app.services.ai_service import classify_ticket_ai
import json
import re


# 🔹 Helper: Safe JSON extraction from AI response
def extract_json(text: str):
    try:
        match = re.search(r"\{.*?\}", text, re.DOTALL)

        if not match:
            print("No JSON found in AI response:", text)
            return {"priority": "medium", "category": "general"}

        return json.loads(match.group())

    except Exception as e:
        print("JSON PARSE ERROR:", e)
        print("RAW AI RESPONSE:", text)
        return {"priority": "medium", "category": "general"}


# 🔹 CREATE Ticket
async def create_ticket(data):
    try:
        ai_response = await classify_ticket_ai(data.description)

        print("AI RAW RESPONSE:", ai_response)  # 🔍 debug

        ai_data = extract_json(ai_response)

        # ✅ safer access using .get()
        priority = ai_data.get("priority", data.priority)
        category = ai_data.get("category", "general")

        ticket = Ticket(
            title=data.title,
            description=data.description,
            priority=priority,
            category=category
        )

        ticket.save()

        return {
            "success": True,
            "data": {
                "id": str(ticket.id),  # type: ignore
                "title": ticket.title,
                "description": ticket.description,
                "priority": ticket.priority,
                "category": ticket.category
            }
        }

    except Exception as e:
        print("AI ERROR:", e)
        raise HTTPException(status_code=500, detail="AI processing failed")
    

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
                "priority": ticket.priority,
                "category": ticket.category
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
        ticket.category = data.category

        # optional priority update
        if data.priority:
            ticket.priority = data.priority

        ticket.save()

        return {
            "id": str(ticket.id),  # type: ignore
            "title": ticket.title,
            "description": ticket.description,
            "priority": ticket.priority,
            "category": ticket.category
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