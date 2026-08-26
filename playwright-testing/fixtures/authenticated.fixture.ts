import { expect, test as base } from '@playwright/test';
import { InventoryPage } from '../pages/inventory';
import { LoginPage } from '../pages/login_page';
import { sauceDemoData } from '../test-data/saucedemo.data';

type AuthenticatedFixtures = { inventoryPage: InventoryPage };

export const test = base.extend<AuthenticatedFixtures>({
  inventoryPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(
      sauceDemoData.credentials.username,
      sauceDemoData.credentials.password
    );
    await expect(page).toHaveURL(/inventory\.html$/);
    await use(new InventoryPage(page));
  },
});

export { expect };
