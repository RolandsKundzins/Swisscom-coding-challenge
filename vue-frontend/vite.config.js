import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [
    vue({
      template: {
        compilerOptions: {
          // Ignore sdx-web-components from vue compiler
          isCustomElement: (tag) => tag.startsWith('sdx-'),
        },
      },
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    host: '0.0.0.0', // Ensure Vite is accessible in Docker
    strictPort: true,
    port: 5173,
    allowedHosts: ['vue-frontend'], // Allow Playwright to access Vite
  },
});
