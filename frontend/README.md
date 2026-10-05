# SubLinkHQ Frontend

The frontend application for SubLinkHQ, built with Next.js.

## Tech Stack

* React Vite
* TypeScript
* Docker

## Project Structure

```text
frontend/
├── app/
├── public/
├── package.json
├── Dockerfile
└── ...
```

## Running with Docker

From the project root:

```bash
docker compose --env-file ./backend/.env up --build frontend
```

The application will be available at:

```text
http://localhost:5173
```

## Running the Full Application

From the project root:

```bash
docker compose --env-file ./backend/.env up --build
```

This starts the frontend, backend, and PostgreSQL services.
