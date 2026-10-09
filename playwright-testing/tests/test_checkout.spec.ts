import { expect } from '@playwright/test';
import { test } from '../fixtures/authenticated.fixture';
import { CartPage } from '../pages/cart_page';
import { CheckoutStepOne } from '../pages/checkout_step_one_page';
import { CheckoutStepTwo } from '../pages/checkout_step_two_page';
import { CheckoutComplete } from '../pages/checkout_complete';
import { sauceDemoData } from '../test-data/saucedemo.data';
import { allure } from 'allure-playwright';

const checkout = sauceDemoData.checkout;

// 同一段結帳流程，用不同的商品組合各跑一次
const checkoutCases = [
    {
        title: 'test_tc010 - Single Item Checkout',
        story: 'Single Item Checkout',
        severity: 'critical',
        items: checkout.singleItems,
        summary: checkout.singleItemSummary,
    },
    {
        title: 'test_tc015 - Multiple Item Checkout',
        story: 'Multiple Item Checkout',
        severity: 'normal',
        items: checkout.multipleItems,
        summary: checkout.multipleItemSummary,
    },
];

test.describe('Checkout Test', () => {

    for (const { title, story, severity, items, summary } of checkoutCases) {

        test(title, { tag: ['@smoke', '@regression'] }, async ({ inventoryPage, page }) => {
            await allure.epic('SauceDemo Project');
            await allure.feature('Checkout');
            await allure.story(story);
            await allure.severity(severity);
            await allure.tag('smoke');
            await allure.tag('regression');

            // Add items to cart
            for (const item of items) {
                await inventoryPage.addToCart(item.name);
            }

            await expect(
                inventoryPage.shoppingCartLink,
                `Cart count is not ${items.length} after adding items`
            ).toContainText(String(items.length));

            await inventoryPage.shoppingCartLink.click();
            await expect(page).toHaveURL('/cart.html');

            // Cart validation
            const cartPage = new CartPage(page);
            const itemsInCart = await cartPage.getAllItemsDetail();

            expect(
                itemsInCart,
                `Expected ${items.length} items, actually ${itemsInCart.length} items`
            ).toHaveLength(items.length);
            expect(itemsInCart).toEqual(items);

            // Checkout Step One
            await cartPage.clickCheckout();

            const step1Page = new CheckoutStepOne(page);

            await expect(step1Page.checkoutTitle).toHaveText('Checkout: Your Information');
            await expect(step1Page.firstName).toBeVisible();
            await expect(step1Page.lastName).toBeVisible();
            await expect(step1Page.zipCode).toBeVisible();
            await expect(step1Page.continueBtn).toBeVisible();

            await step1Page.fillCheckoutInformation(
                checkout.customer.firstName,
                checkout.customer.lastName,
                checkout.customer.postalCode
            );
            await step1Page.clickContinue();

            // Checkout Step Two
            const step2Page = new CheckoutStepTwo(page);

            await expect(step2Page.finishButton).toBeVisible();
            await expect(step2Page.cancelButton).toBeVisible();

            const itemsInCheckout = await step2Page.getCheckoutItemsDetail();

            expect(
                itemsInCheckout,
                `Expected ${items.length} items, actually ${itemsInCheckout.length} items`
            ).toHaveLength(items.length);
            expect(itemsInCheckout).toEqual(items);

            // Payment & Shipping validation
            expect(
                await step2Page.getPaymentInfo(),
                'Payment info mismatch'
            ).toContain(checkout.paymentInfo);

            expect(
                await step2Page.getShippingInfo(),
                'Shipping info mismatch'
            ).toBe(checkout.shippingInfo);

            // Financial summary validation
            expect(await step2Page.getItemTotal(), 'Item total mismatch').toBe(summary.itemTotal);
            expect(await step2Page.getTax(), 'Tax mismatch').toBe(summary.tax);
            expect(await step2Page.getTotal(), 'Total mismatch').toBe(summary.total);

            // Finish checkout
            await step2Page.clickFinish();

            const completePage = new CheckoutComplete(page);

            await expect(page).toHaveURL('/checkout-complete.html');

            // Checkout complete validation
            await expect(completePage.completeTitle).toHaveText('Checkout: Complete!');
            await expect(completePage.completeHeader).toHaveText('Thank you for your order!');
            await expect(completePage.completeText).toHaveText(
                'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
            );

            // Back to inventory
            await completePage.clickBackHomeBtn();
            await expect(page).toHaveURL('/inventory.html');
        });
    }

});
