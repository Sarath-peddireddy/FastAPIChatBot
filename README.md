# LLM-Powered Chatbot with FastAPI and SQL

This project implements a chatbot that uses Groq's LLM to process natural language queries and retrieve data from a SQLite database.

## Project Structure
```
.
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
└── README.md
```

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

## Features
- Natural language query processing using Groq's LLM
- SQLite database integration
- React frontend for user interaction
- Error handling and logging
- Environment variable configuration

## API Endpoints
- POST `/api/query`: Process natural language queries
- GET `/api/customers`: Retrieve all customers
- POST `/api/customers`: Add new customer

## Technologies Used
- Backend: FastAPI, SQLite3, Groq LLM
- Frontend: ReactJS
- Database: SQLite3 