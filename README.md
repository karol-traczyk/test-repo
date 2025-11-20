# test-repo

## Simple Node Server

This repository now includes a minimal Express-based HTTP server to support the "New flow test" task.

### Routes
- `GET /` → plain text `Hello from the simple Node server`
- `GET /health` → JSON `{ "status": "ok" }`

### Running the server
- `npm install` to install dependencies
- `npm start` to run in production mode (defaults to port `3000`, override with `PORT=4000 npm start`)
- `npm run dev` to run in development mode with automatic reloads via `nodemon`

Both scripts log the active port on startup and log each incoming request. Unexpected errors are logged and return a generic 500 JSON response.
