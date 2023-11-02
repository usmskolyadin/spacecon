import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import dotenv from 'dotenv';

export default defineConfig(({ mode }) => {
  // Load environment variables only in development mode
  if (mode === 'development') {
    dotenv.config();
  }

  // Other Vite configuration...
  return {
    plugins: [react()]
  };
});