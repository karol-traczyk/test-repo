const dotenv = require('dotenv');

dotenv.config();

const config = {
  env: process.env.NODE_ENV || 'development',
  port: Number.parseInt(process.env.PORT, 10) || 3000,
  serviceName: process.env.SERVICE_NAME || 'basic-server',
};

module.exports = config;
