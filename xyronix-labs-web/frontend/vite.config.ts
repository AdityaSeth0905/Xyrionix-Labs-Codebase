import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: '0.0.0.0',  // Ensures the app is accessible externally
    port: 5173,       // Ensure this matches your Render config
  },
})
