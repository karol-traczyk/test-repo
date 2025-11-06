import { serve } from "https://deno.land/std@0.208.0/http/server.ts";
import { handler } from "./handler.ts";

// Get port from environment variable or use default 8080
const PORT = parseInt(Deno.env.get("PORT") || "8080");

// Only run the server if this module is executed directly
if (import.meta.main) {
  // Setup graceful shutdown
  const abortController = new AbortController();

  // Handle shutdown signals
  const shutdown = () => {
    console.log("\nReceived shutdown signal, closing server gracefully...");
    abortController.abort();
  };

  Deno.addSignalListener("SIGINT", shutdown);
  Deno.addSignalListener("SIGTERM", shutdown);

  // Start the server
  console.log(`HTTP server listening on http://localhost:${PORT}`);

  try {
    await serve(handler, {
      port: PORT,
      signal: abortController.signal,
      onListen: ({ port }) => {
        console.log(`Server started on port ${port}`);
      },
    });
  } catch (error) {
    // Handle abort error gracefully
    if (error instanceof Error && error.name === "AbortError") {
      console.log("Server closed successfully");
    } else {
      console.error("Server error:", error);
      Deno.exit(1);
    }
  }

  console.log("Shutdown complete");
  Deno.exit(0);
}
