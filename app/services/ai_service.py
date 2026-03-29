import httpx
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


async def classify_ticket_ai(description: str):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Classify the support ticket and assign priority.

    Ticket: {description}

    Return JSON:
    {{
        "category": "...",
        "priority": "low/medium/high"
    }}
    """

    data = {
        "model": "mistralai/mixtral-8x7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    return content