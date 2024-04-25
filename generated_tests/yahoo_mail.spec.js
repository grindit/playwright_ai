import { test, expect } from '@playwright/test';

test('Yaho Mail Test', async ({ page }) => {
  await page.goto('https://www.yahoo.com');
  await page.click('button[name="agree"]');
  await page.click('id=ybarMailLink');
  await expect(page.url()).toBe('https://mail.yahoo.com/');
});