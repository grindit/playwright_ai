// Import the necessary modules from Playwright
const { test, expect } = require('@playwright/test');

// Define the test suite
test.describe('GitHub Search Test', () => {

  // Define a test case
  test('should navigate to the Playwright GitHub repository and check for repository name', async ({ page }) => {

    // Navigate to GitHub
    await page.goto('https://github.com/');

    await page.getByRole('button', { name: 'Search or jump to...' }).click();
    await page.getByRole('combobox', { name: 'Search' }).click();
    await page.getByRole('combobox', { name: 'Search' }).fill('playwright');
    await page.getByRole('combobox', { name: 'Search' }).press('Enter');

    // Wait for the results to be displayed and click on the correct link
    await page.waitForSelector('text=microsoft/playwright');
    await page.click('text=microsoft/playwright');

    // Assert that the Playwright repository page is displayed
    await expect(page).toHaveURL(/.*microsoft\/playwright/);

    // Verify repository name is displayed on the page
    //await expect(page.locator('h1')).toContainText('playwright');

  });
});