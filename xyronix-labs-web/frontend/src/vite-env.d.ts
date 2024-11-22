/// <reference types="vite/client" />
export default defineConfig({
    server: {
      host: '0.0.0.0',  // Ensures the app is accessible externally
      port: 5173,       // Ensure this matches your Render config
    }
  });
  