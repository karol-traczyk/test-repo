# Deno HTTP Server

A simple, reliable HTTP server built with Deno that demonstrates basic routing
and graceful shutdown.

## Features

- Two endpoints:
  - `GET /` - Returns "Hello from Deno"
  - `GET /health` - Returns "ok" (health check endpoint)
- Configurable port via environment variable
- Graceful shutdown on SIGINT/SIGTERM
- Minimal permissions required
- Clean, readable code
- Comprehensive tests

## Prerequisites

- [Deno](https://deno.land/) installed (1.0 or higher)

## Running Locally

### Default Configuration (port 8080)

```bash
deno run --allow-net --allow-env main.ts
```

The server will start on `http://localhost:8080`.

### Custom Port Configuration

```bash
PORT=3000 deno run --allow-net --allow-env main.ts
```

The server will start on the specified port (e.g., `http://localhost:3000`).

## Testing the Endpoints

Once the server is running, you can test the endpoints:

```bash
# Test the root endpoint
curl http://localhost:8080/

# Test the health endpoint
curl http://localhost:8080/health
```

## Running Tests

Run the test suite with:

```bash
deno test --allow-net --allow-env
```

All tests should pass, verifying that both endpoints return the expected
responses.

## Code Quality

### Format Code

```bash
deno fmt
```

### Lint Code

```bash
deno lint
```

## Graceful Shutdown

The server handles SIGINT (Ctrl+C) and SIGTERM signals gracefully:

- Logs the shutdown initiation
- Closes the server cleanly
- Exits with status code 0

To stop the server, press `Ctrl+C` in the terminal.

## Permissions

This server requires minimal permissions:

- `--allow-net` - For network access to run the HTTP server
- `--allow-env` - For reading the PORT environment variable

## Project Structure

```
.
├── main.ts         # Main server implementation
├── main_test.ts    # Test suite
└── README.md       # This file
```

## API Documentation

### GET /

Returns a plain text greeting.

**Response:**

- Status: 200 OK
- Content-Type: text/plain
- Body: `Hello from Deno`

### GET /health

Health check endpoint for monitoring.

**Response:**

- Status: 200 OK
- Content-Type: text/plain
- Body: `ok`

### Other Routes

Any other route will return a 404 Not Found response.
