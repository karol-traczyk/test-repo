import { assertEquals } from "https://deno.land/std@0.208.0/assert/mod.ts";
import { serve } from "https://deno.land/std@0.208.0/http/server.ts";

// Handler function from main.ts (extracted for testing)
function handler(req: Request): Response {
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

// Helper function to start a test server on a random port
async function startTestServer(): Promise<
  { port: number; shutdown: () => void }
> {
  const abortController = new AbortController();

  // Use a fixed port for testing to avoid race conditions
  const testPort = 8888 + Math.floor(Math.random() * 1000);

  // Start the server (we keep the promise for cleanup but don't need to assign it)
  serve(handler, {
    port: testPort,
    signal: abortController.signal,
    onListen: () => {},
  });

  // Give server a moment to start
  await new Promise((resolve) => setTimeout(resolve, 100));

  return {
    port: testPort,
    shutdown: () => {
      abortController.abort();
    },
  };
}

Deno.test("GET / returns 'Hello from Deno'", async () => {
  const { port, shutdown } = await startTestServer();

  try {
    const response = await fetch(`http://localhost:${port}/`);
    const text = await response.text();

    assertEquals(response.status, 200);
    assertEquals(text, "Hello from Deno");
    assertEquals(response.headers.get("content-type"), "text/plain");
  } finally {
    shutdown();
    // Give server time to cleanup
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
});

Deno.test("GET /health returns 'ok'", async () => {
  const { port, shutdown } = await startTestServer();

  try {
    const response = await fetch(`http://localhost:${port}/health`);
    const text = await response.text();

    assertEquals(response.status, 200);
    assertEquals(text, "ok");
    assertEquals(response.headers.get("content-type"), "text/plain");
  } finally {
    shutdown();
    // Give server time to cleanup
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
});

Deno.test("GET /unknown returns 404", async () => {
  const { port, shutdown } = await startTestServer();

  try {
    const response = await fetch(`http://localhost:${port}/unknown`);
    const text = await response.text();

    assertEquals(response.status, 404);
    assertEquals(text, "Not Found");
  } finally {
    shutdown();
    // Give server time to cleanup
    await new Promise((resolve) => setTimeout(resolve, 100));
  }
});
