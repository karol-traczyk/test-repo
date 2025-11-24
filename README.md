# test-repo

Minimal Express-based HTTP server with a `/health` endpoint and environment-driven configuration.

## Getting Started

1. Install dependencies:
   ```
   npm install
   ```
2. Copy `.env.example` to `.env` and adjust the values (at least `PORT` and optionally `SERVICE_NAME`).

## Development

Run the server with automatic reloads:
```
npm run dev
```
The server listens on the configured `PORT` and logs requests in a developer-friendly format.

## Production

Run the server in production mode:
```
npm start
```
This uses the `NODE_ENV=production` profile, enabling stricter logging and production-ready defaults.

## Health Check

Send a `GET` request to `/health` to verify the service is running. It returns a JSON payload with status, service name, uptime, and timestamp.
