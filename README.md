# LLM-Powered Chatbot with FastAPI and SQL

This project implements a chatbot that uses Groq's LLM to process natural language queries and retrieve data from a SQLite database. The system converts natural language questions into SQL queries and displays the results in a user-friendly interface.

## Features

- Natural language to SQL query conversion using Groq's LLM
- FastAPI backend with SQLite database
- React frontend with Material-UI components
- Real-time query processing and results display
- Error handling and logging
- Environment variable configuration
- CORS support for local development

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- SQLite3
- Groq LLM (llama-3.1-8b-instant model)
- Python 3.8+

### Frontend
- React
- Material-UI
- Axios
- Node.js 14+

## Project Structure
```
.
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI application
│   │   ├── database.py      # Database operations
│   │   ├── models.py        # SQLAlchemy models
│   │   └── utils.py         # Utility functions
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
├── frontend/
│   ├── public/             # Static files
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.js          # Main React component
│   │   └── index.js        # React entry point
│   └── package.json        # Node dependencies
├── .gitignore             # Git ignore rules
├── .env.example           # Example environment variables
└── README.md             # Project documentation
```

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Node.js 14 or higher
- Groq API key

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix/MacOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
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

## Usage

1. Open your browser and go to http://localhost:3000
2. Enter natural language queries in the input field, such as:
   - "Show me all female customers from Mumbai"
   - "List all male customers"
   - "Find customers from New York"
   - "Show me all customers from London"
   - "Find female customers from Tokyo"

3. The system will:
   - Convert your natural language query to SQL
   - Execute the query against the database
   - Display both the generated SQL and results

## Database Schema

The application uses a SQLite database with the following schema:

```sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    location TEXT
);
```

Sample data is automatically seeded when the application starts.

## Environment Variables

Create a `.env` file in the backend directory with the following variables:
```
GROQ_API_KEY=your_groq_api_key_here
```

## API Endpoints

- `POST /api/query`: Process natural language queries
  - Request body: `{"query": "your natural language query"}`
  - Response: `{"status": "success", "query": "original query", "sql_query": "generated SQL", "results": [...]}`

- `GET /api/customers`: Get all customers
  - Response: List of all customers in the database

## Error Handling

The application includes comprehensive error handling for:
- Invalid queries
- SQL execution errors
- API connection issues
- Database errors

All errors are logged and returned with appropriate HTTP status codes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Groq for providing the LLM API
- FastAPI for the backend framework
- React and Material-UI for the frontend components 