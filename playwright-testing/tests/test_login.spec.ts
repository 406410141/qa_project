import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login_page';
import { sauceDemoData } from '../test-data/saucedemo.data';



// [新增] tag：可用 npx playwright test --grep @regression 篩選
test('test_tc002 - Login Info', { tag: ['@regression'] }, async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();
    await loginPage.navigate(loginPage.url);

    await expect(loginPage.allUsernames).toBeVisible();
    await expect(loginPage.allPassword).toBeVisible();

    for (const user of sauceDemoData.credentials.displayedUsers) {
        await expect(loginPage.allUsernames).toContainText(user);
    }

    await expect(loginPage.allPassword)
        .toContainText(sauceDemoData.credentials.password);
});



// [新增] tag：可用 npx playwright test --grep @regression 篩選
test('test_tc003 - Login', { tag: ['@regression'] }, async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(
        loginPage.acceptedUsername,
        loginPage.acceptedPassword
    );

    await expect(page).toHaveURL(
        'https://www.saucedemo.com/inventory.html'
    );
});

// [新增] tag：可用 npx playwright test --grep @regression 篩選
test('test_tc004 - Close Error Message', { tag: ['@regression'] }, async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.navigate(loginPage.url);

    await loginPage.loginButton.click();

    await expect(loginPage.errorContainer).toBeVisible();

    await loginPage.closeErrorButton.click();

    await expect(loginPage.errorContainer).not.toBeVisible();
});