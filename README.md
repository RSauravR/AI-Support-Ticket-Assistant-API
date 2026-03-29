# 🎫 AI Support Ticket Assistant API

An AI-powered backend system that automatically classifies, prioritizes, and manages support tickets using **FastAPI**, **MongoDB**, and **LLM APIs**.

---

## 🚀 Overview
This project streamlines the IT support process by leveraging Large Language Models (LLMs) to analyze ticket descriptions. It intelligently assigns categories and priority levels, ensuring that critical issues are addressed first without manual intervention.

### Core Features
* **Create Support Tickets:** Seamless ingestion of user issues.
* **AI-Based Classification:** Automatically determines **Priority** (Low, Medium, High) and **Category** (Authentication, Billing, Technical, General).
* **Smart Filtering:** Retrieve tickets based on their priority level.
* **Full CRUD Support:** Update or delete tickets as needed.
* **High Reliability:** Includes **retry logic** and **intelligent fallbacks** (defaulting to safe values) if the AI service is unavailable.
* **Input Validation:** Powered by Pydantic to ensure data integrity.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | FastAPI (Python) |
| **Database** | MongoDB Atlas (via MongoEngine) |
| **AI Integration** | OpenRouter (LLM API) |
| **Server** | Uvicorn |
| **Validation** | Pydantic |

---

## 📂 Project Structure

```text
app/
├── main.py                # Entry point & FastAPI initialization
├── models/
│   └── ticket_model.py    # MongoEngine database models
├── schemas/
│   └── ticket_schema.py   # Pydantic models for request/response validation
├── routes/
│   └── ticket_routes.py   # API endpoint definitions
└── services/
    ├── ticket_service.py  # Business logic for ticket operations
    └── ai_service.py      # LLM logic & error handling