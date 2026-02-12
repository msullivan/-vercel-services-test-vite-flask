import { defineConfig } from "vite";

export default defineConfig({
  server: {
    proxy: {
      "/_/backend": "http://127.0.0.1:5000",
    },
  },
});
