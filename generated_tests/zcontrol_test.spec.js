const { test, expect } = require('@playwright/test');

// Define the test suite
test.describe('Manual test case', () => {

  // Define a test case
  test('Manual test case. As a refference', async ({ page }) => {

    // Generate code to open google.com page
    await page.goto('https://www.google.com');

    // Generate code to confirm cookie policy on google.com
    await page.click('button[id="L2AGLb"]');

    // Generate code to click on a <textarea> and search for "Playwright" text on google.com
    await page.click('textarea');
    await page.fill('textarea', 'Playwright');
    await page.press('textarea', 'Enter');

  });
});