const { test, expect} = require('@playwright/test');

test.describe('<Test Name>', () => {

  test('<Test Case Description>', async ({ page }) => {
    page.setViewportSize({ width: 1920, height: 1080 });
    //Insert test code here.

  });
});