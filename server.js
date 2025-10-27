const http = require('http');

// Get port from environment or default to 3000
const PORT = process.env.PORT || 3000;

// Create the HTTP server
const server = http.createServer((req, res) => {
  const { method, url } = req;

  // GET /
  if (method === 'GET' && url === '/') {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({
      status: 'ok',
      message: 'Hello from Fresh'
    }));
    return;
  }

  // GET /health
  if (method === 'GET' && url === '/health') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('ok');
    return;
  }

  // 404 for all other routes
  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'Not found' }));
});

// Start the server
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
  console.log(`Access the server at http://localhost:${PORT}`);
});
