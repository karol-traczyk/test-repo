const request = require('supertest');
const { createApp } = require('../src/app');

describe('Simple Node server', () => {
  test('GET / returns hello text response', async () => {
    const app = createApp();

    const response = await request(app).get('/');

    expect(response.status).toBe(200);
    expect(response.text).toBe('Hello from the simple Node server');
    expect(response.headers['content-type']).toMatch(/text\/plain/);
  });

  test('GET /health returns status ok JSON', async () => {
    const app = createApp();

    const response = await request(app).get('/health');

    expect(response.status).toBe(200);
    expect(response.body).toEqual({ status: 'ok' });
    expect(response.headers['content-type']).toMatch(/application\/json/);
  });

  test('Unexpected errors respond with 500 and generic payload', async () => {
    const app = createApp({ injectFaultRoute: true });

    const response = await request(app).get('/__error');

    expect(response.status).toBe(500);
    expect(response.body).toEqual({ error: 'Internal Server Error' });
  });
});
