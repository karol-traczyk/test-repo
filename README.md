# Simple HTTP Server in Go

A minimal, production-friendly HTTP server built with Go's standard library.

## Features

- Simple JSON health check endpoint
- Request logging with method, path, status code, and duration
- Graceful shutdown on SIGINT/SIGTERM
- Configurable port via environment variable
- Production-ready timeouts and middleware

## Quick Start

### Prerequisites

- Go 1.21 or later

### Build

```bash
go build -o server cmd/server/main.go
```

### Run

Run with default port (8080):
```bash
./server
```

Run with custom port:
```bash
PORT=3000 ./server
```

Or run directly without building:
```bash
go run cmd/server/main.go
```

### Test

Check the health endpoint:
```bash
curl http://localhost:8080/
```

Expected response:
```json
{"status":"ok"}
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | The port the server listens on | `8080` |

## API Endpoints

### GET /

Health check endpoint that returns the server status.

**Response:**
```json
{
  "status": "ok"
}
```

**Status Code:** `200 OK`

## Request Logging

Each request is logged with the following format:
```
METHOD PATH - STATUS_CODE - DURATION
```

Example:
```
GET / - 200 - 245.5µs
```

## Graceful Shutdown

The server listens for SIGINT (Ctrl+C) and SIGTERM signals and performs a graceful shutdown with a 10-second timeout. This ensures all in-flight requests complete before the server stops.

## Docker

Build and run with Docker:

```bash
# Build image
docker build -t simple-http-server .

# Run container
docker run -p 8080:8080 simple-http-server

# Run with custom port
docker run -p 3000:3000 -e PORT=3000 simple-http-server
```

## Production Considerations

The server includes several production-friendly features:

- **Read Timeout**: 10 seconds
- **Write Timeout**: 10 seconds
- **Idle Timeout**: 60 seconds
- **Graceful Shutdown**: 10-second deadline for completing in-flight requests
- **Request Logging**: All requests are logged with timing information

## License

MIT
