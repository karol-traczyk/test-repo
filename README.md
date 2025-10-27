# test-repo

A minimal Python HTTP server example with a health check endpoint.

## Overview

This project provides a simple, beginner-friendly Python web server that can be run locally with a single command. It includes a `/health` endpoint for uptime monitoring and service verification.

## Features

- **Health Check Endpoint**: `/health` returns HTTP 200 with `{"status": "ok"}`
- **Welcome Endpoint**: `/` provides basic server information
- **Minimal Dependencies**: Uses only Flask for simplicity
- **Easy to Run**: Single command to start the server

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository (if you haven't already):
```bash
git clone <repository-url>
cd test-repo
```

2. (Optional) Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

Start the server with:
```bash
python3 server.py
```

The server will start on `http://0.0.0.0:8000` (accessible at `http://localhost:8000`).

You should see output like:
```
 * Running on http://0.0.0.0:8000
 * Debug mode: on
```

### Testing the Endpoints

**Health Check Endpoint:**
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{"status":"ok"}
```

**Welcome Endpoint:**
```bash
curl http://localhost:8000/
```

Expected response:
```json
{
  "message": "Welcome to the minimal Python HTTP server",
  "endpoints": {
    "/": "This welcome message",
    "/health": "Health check endpoint"
  }
}
```

### Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## Project Structure

```
.
├── server.py           # Main server implementation
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore patterns
└── README.md          # This file
```

## Technical Details

- **Framework**: Flask 3.0.0 (lightweight Python web framework)
- **Port**: 8000 (configurable in `server.py`)
- **Host**: 0.0.0.0 (accessible from all network interfaces)

## Use Cases

- Local development reference server
- Health check monitoring examples
- Learning basic Python web server concepts
- Testing uptime monitoring tools

## License

This is a minimal example project for demonstration purposes.
