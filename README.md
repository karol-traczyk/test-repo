# Simple Node.js Server

A minimal Node.js HTTP server that responds to HTTP requests with JSON payloads.

## Features

- Simple HTTP server built with Node.js core modules (no external frameworks)
- Responds on configurable port (defaults to 3000)
- Two endpoints:
  - `GET /` - Returns a welcome message
  - `GET /health` - Health check endpoint

## Prerequisites

- Node.js (v14 or higher recommended)
- npm

## Installation

Install the dependencies (nodemon for development):

```bash
npm install
```

## Running the Server

### Production Mode

Start the server in production mode:

```bash
npm start
```

### Development Mode (with auto-reload)

Start the server in development mode with nodemon for automatic restarts on file changes:

```bash
npm run dev
```

## Endpoints

### GET /

Returns a welcome message.

**Response:**
```json
{
  "message": "Hello from Node server"
}
```

### GET /health

Health check endpoint.

**Response:**
```json
{
  "status": "ok"
}
```

## Testing the Endpoints

Once the server is running, you can test the endpoints using curl:

```bash
# Test the root endpoint
curl http://localhost:3000/

# Test the health endpoint
curl http://localhost:3000/health
```

## Configuration

The server listens on the port specified by the `PORT` environment variable, or defaults to port 3000.

To run on a different port:

```bash
PORT=8080 npm start
```

## Project Structure

```
.
├── server.js       # Main server file
├── package.json    # Project configuration and dependencies
├── .gitignore      # Git ignore rules
└── README.md       # This file
```
