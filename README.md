#  AI Support Ticket Assistant API

An AI-powered backend system that automatically classifies, prioritizes, and manages support tickets using **FastAPI**, **MongoDB**, and **LLM APIs**.

---

##  Overview
This project streamlines the IT support process by leveraging Large Language Models (LLMs) to analyze ticket descriptions. It intelligently assigns categories and priority levels, ensuring that critical issues are addressed first without manual intervention.

### Core Features
* **Create Support Tickets:** Seamless ingestion of user issues.
* **AI-Based Classification:** Automatically determines **Priority** (Low, Medium, High) and **Category** (Authentication, Billing, Technical, General).
* **Smart Filtering:** Retrieve tickets based on their priority level.
* **Full CRUD Support:** Update or delete tickets as needed.
* **High Reliability:** Includes **retry logic** and **intelligent fallbacks** (defaulting to safe values) if the AI service is unavailable.
* **Input Validation:** Powered by Pydantic to ensure data integrity.

---

##  Tech Stack

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

# AI Support Ticket Assistant API

An AI-powered backend system that automatically classifies support tickets using **FastAPI**, **MongoDB**, and **LLM APIs**. This project is designed to bridge the gap between raw user input and organized, prioritized data.

---

## ⚙️ Setup Instructions

Follow these steps to get the environment running locally:

1. **Clone the Repository**
   git clone <your-repo-url>
   cd AI-Support-Ticket-Assistant-API

2. **Create Virtual Environment**
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On Mac/Linux: source venv/bin/activate

3. **Install Dependencies**
   pip install -r requirements.txt

4. **Setup Environment Variables**
   Create a .env file in the root directory and add the following:
   MONGO_URI=your_mongodb_connection_string
   OPENROUTER_API_KEY=your_api_key

5. **Run the Server**
   python -m uvicorn app.main:app --reload

6. **Open API Docs**
   Access the interactive Swagger documentation at: http://127.0.0.1:8000/docs

---

## 🔌 API Endpoints

- **Create Ticket** (POST /tickets): Submits a ticket for AI classification and storage.
- **Get All Tickets** (GET /tickets): Retrieves all tickets from the database.
- **Filter Tickets** (GET /tickets?priority=high): Filters tickets by their assigned priority.
- **Update Ticket** (PUT /tickets/{id}): Updates existing ticket details.
- **Delete Ticket** (DELETE /tickets/{id}): Removes a ticket from the system.

---

## 🧠 AI Functionality

The core logic uses an LLM to automatically process ticket descriptions:
- **Priority Classification:** Low, Medium, High.
- **Category Assignment:** Authentication, Billing, Technical, General.

### 🛠️ Reliability Features
To ensure the system remains robust even if the AI service is unstable:
- **Retry Logic:** Automatic re-attempts for failed AI API calls.
- **JSON Extraction:** Parses clean data even from non-structured AI text responses.
- **Fallback Defaults:** Graceful degradation to default values if the AI fails completely.
- **Output Validation Layer:** Ensures all data meets the required schema before saving.

### 📝 Example Response
{
  "success": true,
  "data": {
    "id": "123",
    "title": "Login issue",
    "priority": "high",
    "category": "authentication"
  }
}

---

## 🔮 Future Improvements
- AI-generated automated response suggestions.
- Ticket summarization for long descriptions.
- Analytics dashboard for support volume trends.
- Authentication and user roles for security.

---

## 🎓 Learnings
This project highlights several key backend and AI integration skills:
- **Backend API Design:** Structuring a clean, asynchronous API with FastAPI.
- **Database Management:** Integrating MongoDB using the MongoEngine ODM.
- **AI Integration:** Effectively communicating with LLM APIs for classification tasks.
- **Defensive Programming:** Implementing reliability patterns to handle non-deterministic AI outputs.

---

## 📜 License
This project is for learning and demonstration purposes.

**Author:** Saurav R R