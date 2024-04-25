import { test, expect } from '@playwright/test';

test('Gooogle detailes search test', async ({ page }) => {
  await page.goto('https://www.google.com');
  await page.click('button#L2AGLb');
  await page.click('textarea[name="q"]');
  await page.fill('textarea[name="q"]', 'playwright');
  await page.waitForSelector('input[name="btnK"]');
  await page.press('input[name="btnK"]', 'Enter');
  await page.waitForSelector('div#result-stats');
  const searchResults = await page.$$('div[data-async-context]');

  let containsPlaywright = false;
  for (const result of searchResults) {
    const text = await result.textContent();
    if (text.includes('playwright')) {
      containsPlaywright = true;
      break;
    }
  }

  expect(containsPlaywright).toBeTruthy();
  await page.screenshot({ path: 'screenshot.png' });
});