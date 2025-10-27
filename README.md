# Fresh Server

A minimal Node.js HTTP server built with the native `http` module.

## Requirements

- Node.js LTS (v14 or higher recommended)

## Installation

While this project has no external dependencies, you can still run:

```bash
npm install
```

## Running the Server

Start the server with:

```bash
npm start
```

The server will run on port 3000 by default.

### Environment Variables

- `PORT` - Override the default port (3000)

Example:

```bash
PORT=8080 npm start
```

## Endpoints

### GET /

Returns a JSON status message.

**Response:**
```json
{
  "status": "ok",
  "message": "Hello from Fresh"
}
```

**Example:**
```bash
curl http://localhost:3000/
```

### GET /health

Returns a simple health check response.

**Response:**
```
ok
```

**Example:**
```bash
curl http://localhost:3000/health
```

### Unknown Routes

Any unmatched route returns a 404 with JSON error message.

**Response:**
```json
{
  "error": "Not found"
}
```

**Example:**
```bash
curl http://localhost:3000/unknown
```

## Testing

Test all endpoints with curl:

```bash
# Test the main endpoint
curl http://localhost:3000/

# Test the health endpoint
curl http://localhost:3000/health

# Test 404 handling
curl http://localhost:3000/unknown
```
