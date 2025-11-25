const DEFAULT_PORT = 8000;

function getPortFromEnv(): number {
  const rawPort = Deno.env.get("PORT");
  if (!rawPort) {
    return DEFAULT_PORT;
  }

  const port = Number(rawPort);
  if (!Number.isFinite(port) || port <= 0) {
    console.warn(
      `Invalid PORT "${rawPort}" provided. Falling back to ${DEFAULT_PORT}.`,
    );
    return DEFAULT_PORT;
  }

  return port;
}

const port = getPortFromEnv();
const headers = { "content-type": "text/plain; charset=utf-8" };

const handler = (req: Request): Response => {
  const { pathname } = new URL(req.url);

  if (req.method === "GET" && pathname === "/health") {
    return new Response("ok", { status: 200, headers });
  }

  if (req.method === "GET" && pathname === "/") {
    return new Response("Hello from Deno", { status: 200, headers });
  }

  return new Response("Not Found", { status: 404, headers });
};

console.log(`HTTP server listening on http://localhost:${port}`);
Deno.serve({ port }, handler);
