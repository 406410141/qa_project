import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/login_page';
import { allure } from 'allure-playwright';

test.describe(' Smoke Tests ', () => {

    test('test_tc001  @smoke', async ({ page }) => {

        await allure.epic("SauceDemo Project")
        await allure.feature("Home Page")
        await allure.tag("smoke")
        await allure.severity('critical')
        await allure.story(" homepage loading")
        const loginPage = new LoginPage(page);

        await loginPage.navigate(loginPage.url);

        await expect(
            loginPage.logo,
            'Login Logo Not Display'
        ).toBeVisible();

        await expect(
            loginPage.usernameInput,
            'Account Input Field Not Displayed'
        ).toBeVisible();

        await expect(
            loginPage.passwordInput,
            'Password Input Field Not Displayed'
        ).toBeVisible();

        await expect(
            loginPage.loginButton,
            'Login BTN Not Displayed'
        ).toBeVisible();
    });

});