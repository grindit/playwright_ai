// Import the necessary modules from Playwright
const { test, expect } = require('@playwright/test');

// Define the test suite
test.describe('Test name', () => {

  // Define a test case
  test('test case description', async ({ page }) => {

    // Go to google.com
    await page.goto('https://www.google.com');

    // Accept cookie policy
    await page.click('text="Zaakceptuj wszystko"');

    // Click on the textarea
    await page.click('textarea');

    // Type 'Playwright' in the textarea
    await page.fill('textarea', 'Playwright');

    // Press Enter to submit the search
    await page.press('textarea', 'Enter');

    // Wait for the search results to load
    await page.waitForSelector('div#search');

    // Check if any search result contains the string 'playwright'
    const searchResults = await page.$$('div#search a');
    let containsPlaywright = false;
    for (const result of searchResults) {
      const text = await result.textContent();
      if (text.toLowerCase().includes('playwright')) {
        containsPlaywright = true;
        break;
      }
    }

    // Assert that at least one search result contains 'playwright'
    expect(containsPlaywright).toBeTruthy();

  });
});