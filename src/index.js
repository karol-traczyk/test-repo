const http = require('http');
const config = require('./config');
const createServer = require('./server');

const app = createServer(config);
const server = http.createServer(app);

server.listen(config.port, () => {
  console.log(
    `${config.serviceName} listening on port ${config.port} (${config.env} mode)`
  );
});

const gracefulShutdown = (signal) => {
  console.log(`Received ${signal}. Shutting down gracefully...`);
  server.close(() => {
    console.log('Server closed. Goodbye!');
    process.exit(0);
  });
};

['SIGTERM', 'SIGINT'].forEach((signal) => {
  process.on(signal, () => gracefulShutdown(signal));
});
