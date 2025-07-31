# VMS (Visitor Management System)

A FastAPI-based Visitor Management System (VMS) for managing user authentication and visitor records, using SQLAlchemy ORM and JWT authentication.

## Features
- User authentication with JWT tokens
- Password hashing with bcrypt
- RESTful API endpoints for login and user management
- SQLAlchemy ORM for database operations
- Docker support for containerization
- Redis integration (optional)

## Tech Stack
- Python 3.12+
- FastAPI
- SQLAlchemy
- Passlib (bcrypt)
- PyJWT (jose)
- Docker
- Redis (optional)

## Getting Started

### Prerequisites
- Python 3.12+
- Docker (optional)
- Redis (optional)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd internship-project/vms
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   - By default, uses SQLite (`vms.db`).
   - Update `database.py` for other DBs if needed.

### Running the Application
```bash
uvicorn main:app --reload
```

### Using Docker
Build and run the container:
```bash
docker build -t vms .
docker run -p 8000:8000 vms
```

## API Endpoints
- `/login` : Obtain JWT token
- `/users` : User management (see `routes.py`)
- Other endpoints as defined in `routes.py`

## Authentication
- Uses OAuth2 with JWT Bearer tokens
- Passwords are hashed using bcrypt

## Project Structure
```
vms/
  ├── auth.py          # Authentication logic
  ├── database.py      # Database setup
  ├── main.py          # FastAPI app entrypoint
  ├── models.py        # SQLAlchemy models
  ├── redis_client.py  # Redis integration
  ├── routes.py        # API routes
  ├── schemas.py       # Pydantic schemas
  ├── requirements.txt # Python dependencies
  ├── Dockerfile       # Docker configuration
  └── vms.db           # SQLite database
```

## License
This project is for interview and educational purposes.
