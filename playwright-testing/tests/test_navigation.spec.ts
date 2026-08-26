import { expect } from '@playwright/test';
import { test } from '../fixtures/authenticated.fixture';
import { sauceDemoData } from '../test-data/saucedemo.data';
import { allure } from 'allure-playwright';

test.describe('Navigation Bar Tests', () => {

    test('test_tc005 - Check Nav Bar Items', async ({ inventoryPage }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Navigation Bar');
        await allure.story('Check Nav Bar Items');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.openSideMenu();

        for (
            let i = 0;
            i < sauceDemoData.navigation.menuItems.length;
            i++
        ) {
            await expect(
                inventoryPage.sidebarContainer.locator('a').nth(i)
            ).toHaveText(
                sauceDemoData.navigation.menuItems[i]
            );
        }

        await inventoryPage.closeSideMenu();

        await expect(
            inventoryPage.sidebarContainer
        ).not.toBeVisible();
    });


    test('test_tc006 - Check Nav Bar About', async ({ inventoryPage, page }) => {
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


    test('test_tc007 - Check Nav Bar Logout', async ({ inventoryPage, page }) => {
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