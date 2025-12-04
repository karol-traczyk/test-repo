# test-repo
Refresh

## Contents
- [Node.js tips](#nodejs-tips)

## Node.js tips
Use these battle-tested notes before shipping or debugging a Node.js service.

### Async/await best practices
- Keep async flows linear with `async/await`; wrap parallel work with `Promise.all` to avoid callback pyramids.
- Always return promises from utility functions so callers can await or compose them.

```js
export async function getUserSummary(userId) {
  const [profile, orders] = await Promise.all([
    userService.fetchProfile(userId),
    orderService.fetchRecent(userId),
  ]);
  return { profile, orders };
}
```

### Error handling patterns
- Centralize Express/Koa error handling and ensure each promise chain has a `.catch` or is awaited inside a `try/catch`.
- Re-throw operational errors with context while letting unexpected exceptions bubble up to the process-level handlers.

```js
app.use(async (req, res, next) => {
  try {
    await routeHandler(req, res);
  } catch (err) {
    next(err);
  }
});

app.use((err, _req, res, _next) => {
  logger.error({ err }, 'request failed');
  res.status(err.statusCode ?? 500).json({ message: 'Something broke' });
});

process.on('unhandledRejection', (err) => {
  logger.fatal({ err }, 'unhandled rejection');
  process.exit(1);
});
```

### Environment variables and configuration
- Load configuration once at startup, validate it, and freeze it so the rest of the codebase reads from a single source of truth.
- Never bake secrets into the repo; rely on `.env` only for local overrides and keep defaults minimal.

```js
import { config } from 'dotenv';
import Joi from 'joi';

config();

const schema = Joi.object({
  NODE_ENV: Joi.string().valid('development', 'test', 'production').required(),
  PORT: Joi.number().default(3000),
  DATABASE_URL: Joi.string().uri().required(),
}).unknown(false);

export const settings = Object.freeze(schema.validate(process.env, { abortEarly: false }).value);
```

### Performance-oriented habits
- Favor streaming over buffering large payloads, and offload CPU-bound work to workers/clusters.
- Avoid sync filesystem/crypto calls inside request paths; they block the event loop.

```js
import { createReadStream } from 'node:fs';
import { pipeline } from 'node:stream/promises';
import { Worker } from 'node:worker_threads';

export async function streamExport(res, path) {
  await pipeline(createReadStream(path), res);
}

export function runHeavyJob(payload) {
  return new Promise((resolve, reject) => {
    const worker = new Worker(new URL('./heavy-job.js', import.meta.url), { workerData: payload });
    worker.once('message', resolve);
    worker.once('error', reject);
  });
}
```

### Debugging and observability
- Use the Node inspector (`node --inspect-brk app.js`) and Chrome DevTools/VS Code to step through async stacks.
- Emit structured logs with correlation IDs so distributed traces are easier to follow.

```bash
node --inspect-brk src/server.js
```

```js
const log = pino();

app.use((req, _res, next) => {
  req.context = { requestId: crypto.randomUUID() };
  log.info({ requestId: req.context.requestId, path: req.path }, 'incoming request');
  next();
});
```
