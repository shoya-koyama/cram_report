import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  reporter: 'html',
  use: {
    baseURL: 'http://127.0.0.1:8000',
    trace: 'on-first-retry',
    screenshot: 'on',
    video: 'on',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
  ],
  webServer: {
    command: 'python3 manage.py migrate --run-syncdb && python3 manage.py runserver 127.0.0.1:8000',
    url: 'http://127.0.0.1:8000',
    reuseExistingServer: !process.env.CI,
    env: {
      DATABASE_URL: `sqlite:///${process.cwd()}/playwright.sqlite3`,
      YOUTUBE_API_KEY: process.env.YOUTUBE_API_KEY || 'playwright-test-key',
      SECRET_KEY: process.env.SECRET_KEY || 'playwright-local-test-secret',
      SUPERUSER_NAME: process.env.SUPERUSER_NAME || 'playwright-test',
      SUPERUSER_EMAIL: process.env.SUPERUSER_EMAIL || 'playwright@example.invalid',
      SUPERUSER_PASSWORD: process.env.SUPERUSER_PASSWORD || 'playwright-test-password',
    },
  },
});
