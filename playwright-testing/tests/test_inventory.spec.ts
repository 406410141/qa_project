import { expect } from '@playwright/test';
import { test } from '../fixtures/authenticated.fixture';
import { sauceDemoData } from '../test-data/saucedemo.data';
import { allure } from 'allure-playwright';

test.describe('Inventory Test', () => {

    test('test_tc011 - Item Sort A-Z', async ({ inventoryPage }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Item Sort');
        await allure.story('A-Z');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.sortBy('az');

        const itemNames =
            await inventoryPage.getAllItemNames();

        expect(
            itemNames,
            'Wrong sort: Not A-Z'
        ).toEqual(
            sauceDemoData.sorting.az
        );
    });


    test('test_tc012 - Item Sort Z-A', async ({ inventoryPage }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Item Sort');
        await allure.story('Z-A');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.sortBy('za');

        const itemNames =
            await inventoryPage.getAllItemNames();

        expect(
            itemNames,
            'Wrong sort: Not Z-A'
        ).toEqual(
            sauceDemoData.sorting.za
        );
    });


    test('test_tc013 - Price Lo-Hi', async ({ inventoryPage }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Item Sort');
        await allure.story('Price Low to High');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.sortBy('lohi');

        const itemPrices =
            await inventoryPage.getAllItemPrices();

        expect(
            itemPrices,
            'Wrong sort: Not Price Low to High'
        ).toEqual(
            sauceDemoData.sorting.priceLowToHigh
        );
    });


    test('test_tc014 - Price Hi-Lo', async ({ inventoryPage }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Item Sort');
        await allure.story('Price High to Low');
        await allure.severity('normal');
        await allure.tag('regression');

        await inventoryPage.sortBy('hilo');

        const itemPrices =
            await inventoryPage.getAllItemPrices();

        expect(
            itemPrices,
            'Wrong sort: Not Price High to Low'
        ).toEqual(
            sauceDemoData.sorting.priceHighToLow
        );
    });

});