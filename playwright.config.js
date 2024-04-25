// playwright.config.js
const { devices } = require('@playwright/test');

module.exports = {
  projects: [
    {
      name: 'Chromium Desktop',
      use: {
        ...devices['Desktop Chrome'],
        headless: false, // Run in headed mode
        viewport: { width: 1920, height: 1080 }
      },
    },
  ],
};
