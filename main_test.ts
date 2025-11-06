import {
  assertEquals,
  assertStringIncludes,
} from "https://deno.land/std@0.208.0/assert/mod.ts";
import { handler } from "./handler.ts";

// Unit tests for handler function (no port binding needed)
Deno.test("handler: GET / returns 200 with 'Hello from Deno'", () => {
  const req = new Request("http://localhost:8080/");
  const response = handler(req);

  assertEquals(response.status, 200);
  assertEquals(response.headers.get("content-type"), "text/plain");

  // Read the response body
  response.text().then((text) => {
    assertEquals(text, "Hello from Deno");
  });
});

Deno.test("handler: GET /health returns 200 with 'ok'", () => {
  const req = new Request("http://localhost:8080/health");
  const response = handler(req);

  assertEquals(response.status, 200);
  assertEquals(response.headers.get("content-type"), "text/plain");

  response.text().then((text) => {
    assertEquals(text, "ok");
  });
});

Deno.test("handler: GET /unknown returns 404", () => {
  const req = new Request("http://localhost:8080/unknown");
  const response = handler(req);

  assertEquals(response.status, 404);
  assertEquals(response.headers.get("content-type"), "text/plain");

  response.text().then((text) => {
    assertEquals(text, "Not Found");
  });
});

Deno.test("handler: POST / returns 404 (method not allowed)", () => {
  const req = new Request("http://localhost:8080/", { method: "POST" });
  const response = handler(req);

  assertEquals(response.status, 404);
  assertEquals(response.headers.get("content-type"), "text/plain");

  response.text().then((text) => {
    assertEquals(text, "Not Found");
  });
});

Deno.test("handler: POST /health returns 404 (method not allowed)", () => {
  const req = new Request("http://localhost:8080/health", { method: "POST" });
  const response = handler(req);

  assertEquals(response.status, 404);
  assertEquals(response.headers.get("content-type"), "text/plain");
});

Deno.test("handler: PUT / returns 404", () => {
  const req = new Request("http://localhost:8080/", { method: "PUT" });
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: DELETE / returns 404", () => {
  const req = new Request("http://localhost:8080/", { method: "DELETE" });
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: PATCH /health returns 404", () => {
  const req = new Request("http://localhost:8080/health", { method: "PATCH" });
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: GET /api/users returns 404", () => {
  const req = new Request("http://localhost:8080/api/users");
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: GET / with query params returns 200", () => {
  const req = new Request("http://localhost:8080/?foo=bar");
  const response = handler(req);

  assertEquals(response.status, 200);

  response.text().then((text) => {
    assertEquals(text, "Hello from Deno");
  });
});

Deno.test("handler: GET /health with query params returns 200", () => {
  const req = new Request("http://localhost:8080/health?check=true");
  const response = handler(req);

  assertEquals(response.status, 200);

  response.text().then((text) => {
    assertEquals(text, "ok");
  });
});

Deno.test("handler: GET /healthcheck returns 404 (exact match required)", () => {
  const req = new Request("http://localhost:8080/healthcheck");
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: GET /Health returns 404 (case sensitive)", () => {
  const req = new Request("http://localhost:8080/Health");
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: OPTIONS / returns 404", () => {
  const req = new Request("http://localhost:8080/", { method: "OPTIONS" });
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: HEAD / returns 404", () => {
  const req = new Request("http://localhost:8080/", { method: "HEAD" });
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: GET /health/ with trailing slash returns 404", () => {
  const req = new Request("http://localhost:8080/health/");
  const response = handler(req);

  assertEquals(response.status, 404);
});

Deno.test("handler: GET // (double slash) returns 404", () => {
  const req = new Request("http://localhost:8080//");
  const response = handler(req);

  assertEquals(response.status, 404);
});

// Async tests that actually read response bodies
Deno.test("handler: verify response body content for /", async () => {
  const req = new Request("http://localhost:8080/");
  const response = handler(req);
  const text = await response.text();

  assertEquals(text, "Hello from Deno");
  assertStringIncludes(text, "Deno");
});

Deno.test("handler: verify response body content for /health", async () => {
  const req = new Request("http://localhost:8080/health");
  const response = handler(req);
  const text = await response.text();

  assertEquals(text, "ok");
  assertEquals(text.length, 2);
});

Deno.test("handler: verify 404 response body", async () => {
  const req = new Request("http://localhost:8080/notfound");
  const response = handler(req);
  const text = await response.text();

  assertEquals(text, "Not Found");
  assertStringIncludes(text, "Not Found");
});

Deno.test("handler: handles different domains correctly", () => {
  const req = new Request("http://example.com/");
  const response = handler(req);

  assertEquals(response.status, 200);
});

Deno.test("handler: handles different ports in URL correctly", () => {
  const req = new Request("http://localhost:3000/");
  const response = handler(req);

  assertEquals(response.status, 200);
});
