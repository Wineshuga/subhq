# SubLinkHQ Backend

The backend API for SubLinkHQ, built with FastAPI and SQLModel.

## Tech Stack

* Python
* FastAPI
* SQLModel
* PostgreSQL
* Docker

## Project Structure

```text
backend/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── main.py
│   └── requirements.txt
├── Dockerfile
└── .env
```

## Environment Variables

Create a `.env` file in the `backend` directory:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=subhq
```

Do not commit `.env` to version control.

## Running with Docker

From the project root:

```bash
docker compose --env-file ./backend/.env up --build backend
```

The API will be available at:

```text
http://localhost:8000
```

Interactive API documentation:

```text
http://localhost:8000/docs
```

## Running the Full Application

From the project root:

```bash
docker compose --env-file ./backend/.env up --build
```

This starts the backend, frontend, and PostgreSQL services.
