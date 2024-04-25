import { test, expect } from '@playwright/test';

test('Yaho Mail Test', async ({ page }) => {
  await page.goto('https://www.yahoo.com');
  await page.press('button[name="agree"]', 'Enter');
  await page.click('a#ybarMailLink');
  await expect(page.url()).toBe('https://mail.yahoo.com/');
});