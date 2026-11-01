import { test, expect } from '@playwright/test';

test('報告書を投稿すると詳細ページに表示される', async ({ page }) => {
  const title = `Playwright テスト ${Date.now()}`;
  const body = 'ローカル環境からの E2E テストです。';

  await page.goto('/');
  await page.getByLabel('生徒氏名：タイトル').fill(title);
  await page.getByLabel('詳細').fill(body);
  await page.getByRole('button', { name: '報告' }).click();

  await expect(page.getByRole('heading', { name: title })).toBeVisible();
  await expect(page.getByText(body)).toBeVisible();
});
