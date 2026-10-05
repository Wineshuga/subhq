# SubLinkHQ

SubLinkHQ is a subscription management platform for tracking subscriptions, services, payments, and renewal dates.

## Project Structure

```text
subhq/
├── backend/
├── docs/
├── frontend/
└── docker-compose.yml
```

## Tech Stack

* Frontend: React vite
* Backend: FastAPI
* Database: PostgreSQL
* Containerization: Docker

## Getting Started

### Prerequisites

* Docker
* Docker Compose

### Environment Variables

Create the required environment file:

```text
backend/.env
```

Example:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=subhq
```

Do not commit your `.env` file.

### Run the Application

From the project root:

```bash
docker compose --env-file ./backend/.env up --build
```

The application will be available at:

* Frontend: http://localhost:3000
* Backend: http://localhost:8000
* API documentation: http://localhost:8000/docs

### Stop the Application

```bash
docker compose down
```

To also remove the PostgreSQL volume:

```bash
docker compose down -v
```

> **Warning:** Removing the volume deletes the PostgreSQL data stored in the Docker volume.
