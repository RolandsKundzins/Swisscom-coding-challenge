import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  use: {
    baseURL: process.env.BASE_URL ? process.env.BASE_URL : 'http://localhost:5173',
    headless: true,
    viewport: { width: 1280, height: 720 },
  },
});
