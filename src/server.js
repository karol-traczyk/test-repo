const express = require('express');

const PORT = process.env.PORT || 3000;
const app = express();

// Simple request logger
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
});

app.get('/', (_req, res) => {
  res.type('text/plain').send('Hello from the simple Node server');
});

app.get('/health', (_req, res) => {
  res.status(200).json({ status: 'ok' });
});

// Graceful error handler
app.use((err, _req, res, _next) => {
  console.error('Unexpected server error:', err);
  res.status(500).json({ error: 'Internal Server Error' });
});

app.listen(PORT, () => {
  console.log(`Simple Node server listening on port ${PORT}`);
});
