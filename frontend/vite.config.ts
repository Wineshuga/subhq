import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
	react(),
	tailwindcss(),],
	server: {
    host: true, // Needed for Docker tracking and port mapping
    port: 5173, // Default Vite port
    watch: {
      usePolling: true, // Ensures hot reload works smoothly inside Docker/WSL
    }
  }
})
