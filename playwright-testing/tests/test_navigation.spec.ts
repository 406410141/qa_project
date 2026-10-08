import { expect } from '@playwright/test';
import { test } from '../fixtures/authenticated.fixture';
import { sauceDemoData } from '../test-data/saucedemo.data';
import { allure } from 'allure-playwright';

test.describe('Navigation Bar Tests', () => {

    // [新增] tag：可用 npx playwright test --grep @regression 篩選
    test('test_tc005 - Check Nav Bar Items', { tag: ['@regression'] }, async ({ inventoryPage }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Navigation Bar');
        await allure.story('Check Nav Bar Items');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.openSideMenu();

        const actualMenuTexts = await inventoryPage.sidebarContainer
            .locator('a')
            .allTextContents();

        for (const expectedItem of sauceDemoData.navigation.menuItems) {
            expect(actualMenuTexts).toContain(expectedItem);
        }

        await inventoryPage.closeSideMenu();
        await expect(inventoryPage.sidebarContainer).not.toBeVisible();
    });


    // [新增] tag：可用 npx playwright test --grep @regression 篩選
    test('test_tc006 - Check Nav Bar About', { tag: ['@regression'] }, async ({ inventoryPage, page }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Navigation Bar');
        await allure.story('About');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.openSideMenu();

        await inventoryPage.aboutLink.click();

        await expect(page).toHaveURL(
            'https://saucelabs.com/'
        );
    });


    // [新增] tag：可用 npx playwright test --grep @smoke 篩選
    test('test_tc007 - Check Nav Bar Logout', { tag: ['@smoke', '@regression'] }, async ({ inventoryPage, page }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Navigation Bar');
        await allure.story('Logout');
        await allure.severity('critical');
        await allure.tag('smoke');
        await allure.tag('regression');
        await inventoryPage.openSideMenu();

        await inventoryPage.logoutLink.click();

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/'
        );
    });

});