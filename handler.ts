// Handler function for HTTP requests
export function handler(req: Request): Response {
  const url = new URL(req.url);

  // Route: GET /
  if (url.pathname === "/" && req.method === "GET") {
    return new Response("Hello from Deno", {
      status: 200,
      headers: { "content-type": "text/plain" },
    });
  }

  // Route: GET /health
  if (url.pathname === "/health" && req.method === "GET") {
    return new Response("ok", {
      status: 200,
      headers: { "content-type": "text/plain" },
    });
  }

  // Route not found
  return new Response("Not Found", {
    status: 404,
    headers: { "content-type": "text/plain" },
  });
}
