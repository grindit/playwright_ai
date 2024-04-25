import { test, expect } from '@playwright/test';

test('Gooogle detailes search test', async ({ page }) => {
  await page.goto('https://www.google.com');
  await page.click('button#L2AGLb');
  await page.click('textarea[name="q"]');
  await page.fill('textarea[name="q"]', 'playwright');
  await page.click('input[name="btnK"]');
  await page.waitForSelector('id=result-stats');
  const results = await page.$$('text=playwright');
  expect(results.length).toBeGreaterThan(0);
  await page.screenshot({ path: 'search_results.png' });
});