const { test, expect } = require('@playwright/test');

test.describe('Test name', () => {
  test('test case description', async ({ page }) => {
    // Go to google.com
    await page.goto('https://www.google.com');

    // Accept cookie policy
    await page.click('text="Zaakceptuj wszystko"');

    // Click on the textarea
    await page.click('textarea');

    // Type "Playwright" in the textarea and press Enter
    await page.fill('textarea', 'Playwright');
    await page.press('textarea', 'Enter');

    // Wait for the search results to load
    await page.waitForSelector('#search');

    // Get the search results
    const searchResults = await page.$$('#search .g');

    // Check if any search result contains the word "playwright"
    let hasPlaywright = false;
    for (const result of searchResults) {
      const resultText = await result.innerText();
      if (resultText.includes('playwright')) {
        hasPlaywright = true;
        break;
      }
    }

    // Assert that at least one search result contains "playwright"
    expect(hasPlaywright).toBeTruthy();
  });
});