const express = require('express');
const morgan = require('morgan');

const createServer = (config) => {
  const app = express();

  const loggerFormat = config.env === 'production' ? 'combined' : 'dev';
  app.use(morgan(loggerFormat));
  app.use(express.json());

  app.get('/health', (req, res) => {
    res.json({
      status: 'ok',
      service: config.serviceName,
      timestamp: new Date().toISOString(),
      uptime: process.uptime(),
    });
  });

  app.use((req, res) => {
    res.status(404).json({ message: 'Not Found' });
  });

  app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ message: 'Internal Server Error' });
  });

  return app;
};

module.exports = createServer;
