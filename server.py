#!/usr/bin/env python3
"""
Minimal Python HTTP Server
A simple example server with a health check endpoint.
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/health')
def health_check():
    """Health check endpoint for uptime monitoring."""
    return jsonify({"status": "ok"}), 200


@app.route('/')
def home():
    """Root endpoint with basic info."""
    return jsonify({
        "message": "Welcome to the minimal Python HTTP server",
        "endpoints": {
            "/": "This welcome message",
            "/health": "Health check endpoint"
        }
    }), 200


if __name__ == '__main__':
    # Run the server on all interfaces, port 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
