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
- Comprehensive test coverage (>=85%)
- Automated CI/CD with GitHub Actions

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

### Run All Tests

```bash
deno test --allow-net --allow-env
```

All tests should pass, verifying that both endpoints return the expected
responses.

### Run Tests with Coverage

```bash
deno test --allow-net --allow-env --coverage=coverage
```

### Generate Coverage Report

After running tests with coverage, generate a detailed report:

```bash
# View coverage summary in terminal
deno coverage coverage

# Generate LCOV report for CI/CD
deno coverage coverage --lcov --output=coverage.lcov

# Generate HTML report for local viewing
deno coverage coverage --html
```

### Coverage Threshold

This project maintains **>=85% line coverage**. The CI pipeline will fail if
coverage drops below this threshold.

Current coverage: **100% line coverage** on all handler logic.

### Test Coverage Details

The test suite includes:

- ✅ Happy path tests for both endpoints (GET / and GET /health)
- ✅ Negative tests for unknown routes (404 responses)
- ✅ HTTP method validation (POST, PUT, DELETE, PATCH, OPTIONS, HEAD)
- ✅ Query parameter handling
- ✅ Path matching edge cases (trailing slashes, case sensitivity)
- ✅ Response body verification
- ✅ Content-type header validation
- ✅ Different URL formats (domains, ports)

## Code Quality

### Format Code

```bash
deno fmt
```

### Check Formatting (CI mode)

```bash
deno fmt --check
```

### Lint Code

```bash
deno lint
```

## Continuous Integration

This project uses GitHub Actions for CI/CD. On every push and pull request, the
following checks run automatically:

1. **Format Check** - Ensures code follows Deno formatting standards
2. **Lint Check** - Catches common issues and enforces best practices
3. **Tests** - Runs the full test suite
4. **Coverage** - Generates coverage reports and enforces >=85% threshold

The CI configuration can be found in `.github/workflows/ci.yml`.

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
├── .github/
│   └── workflows/
│       └── ci.yml       # CI/CD pipeline configuration
├── handler.ts           # HTTP request handler logic
├── main.ts              # Server startup and configuration
├── main_test.ts         # Comprehensive test suite
└── README.md            # This file
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
