import { expect } from '@playwright/test';
import { test } from '../fixtures/authenticated.fixture';
import { CartPage } from '../pages/cart_page';
import { allure } from 'allure-playwright';

test.describe('Cart Tests', () => {

    test('test_tc008 - Click Cart Btn', async ({ inventoryPage, page }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Cart');
        await allure.story('Click Cart Btn');
        await allure.tag('smoke');
        await allure.tag('regression');
        await allure.severity('critical');

        await allure.description(`
            測試目標：點擊購物車圖標，驗證跳轉到購物車頁面
            預期結果：成功跳轉到購物車頁面，且頁面標題顯示 'Your Cart'
        `);

        const cartPage = new CartPage(page);

        await inventoryPage.clickShoppingCart();

        await expect(
            page,
            'Cart Link Redirect Wrong URL'
        ).toHaveURL(
            'https://www.saucedemo.com/cart.html'
        );

        await expect(
            cartPage.cartTitle,
            'Wrong Title'
        ).toHaveText('Your Cart');
    });


    test('test_tc009 - Click CTU BTN', async ({ inventoryPage, page }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Cart');
        await allure.story('Click CTU BTN');
        await allure.tag('regression');
        await allure.severity('normal');

        await allure.description(`
            測試目標：點擊繼續購物按鈕，驗證返回商品列表頁面
            預期結果：成功返回商品列表頁面 (inventory.html)
        `);

        const cartPage = new CartPage(page);

        await inventoryPage.clickShoppingCart();

        await expect(
            page,
            'Cart Link Redirect Wrong URL'
        ).toHaveURL(
            'https://www.saucedemo.com/cart.html'
        );

        await cartPage.clickContinueShopping();

        await expect(
            page,
            "CTU button didn't return to inventory page."
        ).toHaveURL(
            'https://www.saucedemo.com/inventory.html'
        );
    });

});