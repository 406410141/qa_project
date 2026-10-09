import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login_page';
import { sauceDemoData } from '../test-data/saucedemo.data';



test('test_tc002 - Login Info', { tag: ['@regression'] }, async ({ page }) => {
    const loginPage = new LoginPage(page);

    await loginPage.goto();

    await expect(loginPage.allUsernames).toBeVisible();
    await expect(loginPage.allPassword).toBeVisible();

    for (const user of sauceDemoData.credentials.displayedUsers) {
        await expect(loginPage.allUsernames).toContainText(user);
    }

    await expect(loginPage.allPassword)
        .toContainText(sauceDemoData.credentials.password);
});



test('test_tc003 - Login', { tag: ['@regression'] }, async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();
    await loginPage.login(
        loginPage.acceptedUsername,
        loginPage.acceptedPassword
    );

    await expect(page).toHaveURL(
        '/inventory.html'
    );
});

test('test_tc004 - Close Error Message', { tag: ['@regression'] }, async ({ page }) => {
    const loginPage = new LoginPage(page);
    await loginPage.goto();

    await loginPage.loginButton.click();

    await expect(loginPage.errorContainer).toBeVisible();

    await loginPage.closeErrorButton.click();

    await expect(loginPage.errorContainer).not.toBeVisible();
});

// 登入失敗的情境：同一段流程，用不同的帳密組合各跑一次
const invalidLoginCases = [
    {
        title: 'test_tc016 - Login With Wrong Password',
        username: sauceDemoData.credentials.username,
        password: 'wrong_password',
        error: 'Epic sadface: Username and password do not match any user in this service',
    },
    {
        title: 'test_tc017 - Login With Empty Username',
        username: '',
        password: sauceDemoData.credentials.password,
        error: 'Epic sadface: Username is required',
    },
    {
        title: 'test_tc018 - Login With Empty Password',
        username: sauceDemoData.credentials.username,
        password: '',
        error: 'Epic sadface: Password is required',
    },
];

for (const { title, username, password, error } of invalidLoginCases) {
    test(title, { tag: ['@regression', '@negative'] }, async ({ page }) => {
        const loginPage = new LoginPage(page);
        await loginPage.goto();
        await loginPage.login(username, password);

        await expect(loginPage.errorContainer).toHaveText(error);
        await expect(page, 'Should stay on login page').toHaveURL('/');
    });
}
