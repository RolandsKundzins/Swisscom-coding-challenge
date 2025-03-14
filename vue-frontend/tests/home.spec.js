import { test, expect } from '@playwright/test';

test('Homepage should load and display the title and at least one card', async ({ page }) => {
  await page.goto('/');

  await test.step('Check page title', async () => {
    await expect(page.locator('h1.d3')).toHaveText('VueJS+Flask Fullstack Example');
  });

  await test.step('Check first sdx-card', async () => {
    const firstCard = page.locator('sdx-card').first();
    await expect(firstCard).toBeVisible();
  });

  await test.step('Check button inside first sdx-card', async () => {
    const button = page.locator('sdx-button.custom-button').first();

    try {
      await expect(button).toBeVisible();
    } catch (error) {
      console.error('Button not found! Taking a screenshot...');
      await page.screenshot({ path: `test-results/error-screenshot-${Date.now()}.png`, fullPage: true });
      throw error; // Ensure the test still fails
    }
  });
});
