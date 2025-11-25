# test-repo

## Minimal Deno HTTP server
This repo bootstraps a tiny Deno server baseline that can be extended later. It exposes two routes using the standard `Deno.serve` API:

- `GET /` responds with `Hello from Deno`.
- `GET /health` responds with `ok` for health checks.

### Run locally
```bash
deno run --allow-net --allow-env main.ts
```

### Configure the port
The server listens on port `8000` by default. Override it by setting `PORT` before running the command:
```bash
PORT=5050 deno run --allow-net --allow-env main.ts
```
