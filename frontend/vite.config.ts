import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 8000,
    proxy: {
      '/api': {
        target: 'localhost:8888',
        changeOrigin: true
      }
    }
  }
})
