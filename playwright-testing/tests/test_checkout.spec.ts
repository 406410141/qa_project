import { expect } from '@playwright/test';
import { test } from '../fixtures/authenticated.fixture';
import { CartPage } from '../pages/cart_page';
import { CheckoutStepOne } from '../pages/checkout_step_one_page';
import { CheckoutStepTwo } from '../pages/checkout_step_two_page';
import { CheckoutComplete } from '../pages/checkout_complete';
import { sauceDemoData } from '../test-data/saucedemo.data';
import { allure } from 'allure-playwright';

test.describe('Checkout Test', () => {

    test('test_tc010 - Single Item Checkout', async ({ inventoryPage, page }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Checkout');
        await allure.story('Single Item Checkout');
        await allure.severity('critical');
        await allure.tag('smoke');
        await allure.tag('regression');
        // Add item to cart
        await inventoryPage.addBackpackButton.click();

        await expect(
            inventoryPage.shoppingCartLink,
            'Cart count is not 1 after adding item'
        ).toContainText('1');

        await inventoryPage.shoppingCartLink.click();

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/cart.html'
        );

        // Cart validation
        const cartPage = new CartPage(page);

        const itemsInCart =
            await cartPage.getAllItemsDetail();

        expect(
            itemsInCart,
            `Expected 1 Item, Actually ${itemsInCart.length} items`
        ).toHaveLength(1);

        expect(itemsInCart).toEqual(
            sauceDemoData.checkout.singleItems
        );

        // Checkout Step One
        await cartPage.clickCheckout();

        const step1Page = new CheckoutStepOne(page);

        await expect(step1Page.checkoutTitle)
            .toHaveText('Checkout: Your Information');

        await expect(step1Page.firstName).toBeVisible();
        await expect(step1Page.lastName).toBeVisible();
        await expect(step1Page.zipCode).toBeVisible();
        await expect(step1Page.continueBtn).toBeVisible();

        await step1Page.fillCheckoutInformation(
            sauceDemoData.checkout.customer.firstName,
            sauceDemoData.checkout.customer.lastName,
            sauceDemoData.checkout.customer.postalCode
        );

        await step1Page.clickContinue();

        // Checkout Step Two
        const step2Page = new CheckoutStepTwo(page);

        await expect(step2Page.finishButton).toBeVisible();
        await expect(step2Page.cancelButton).toBeVisible();

        const itemsInCheckout =
            await step2Page.getCheckoutItemsDetail();

        expect(
            itemsInCheckout,
            `Expected 1 Item, Actually ${itemsInCheckout.length} items`
        ).toHaveLength(1);

        expect(itemsInCheckout).toEqual(
            sauceDemoData.checkout.singleItems
        );

        // Payment & Shipping validation
        const paymentInfo =
            await step2Page.getPaymentInfo();

        const shippingInfo =
            await step2Page.getShippingInfo();

        expect(
            paymentInfo,
            'Payment info mismatch'
        ).toContain(
            sauceDemoData.checkout.paymentInfo
        );

        expect(
            shippingInfo,
            'Shipping info mismatch'
        ).toBe(
            sauceDemoData.checkout.shippingInfo
        );

        // Financial summary validation
        const itemTotal =
            await step2Page.getItemTotal();

        const tax =
            await step2Page.getTax();

        const total =
            await step2Page.getTotal();

        const expectedSummary =
            sauceDemoData.checkout.singleItemSummary;

        expect(
            itemTotal,
            'Item total mismatch'
        ).toBe(expectedSummary.itemTotal);

        expect(
            tax,
            'Tax mismatch'
        ).toBe(expectedSummary.tax);

        expect(
            total,
            'Total mismatch'
        ).toBe(expectedSummary.total);

        // Finish checkout
        await step2Page.clickFinish();

        const completePage =
            new CheckoutComplete(page);

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/checkout-complete.html'
        );

        // Checkout complete validation
        expect(
            await completePage.getCompleteTitle()
        ).toBe('Checkout: Complete!');

        expect(
            await completePage.getCompleteHeader()
        ).toBe('Thank you for your order!');

        expect(
            await completePage.getCompleteText()
        ).toBe(
            'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        );

        // Back to inventory
        await completePage.clickBackHomeBtn();

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/inventory.html'
        );
    });


    test('test_tc015 - Multiple Item Checkout', async ({ inventoryPage, page }) => {
        await allure.epic('SauceDemo Project');
        await allure.feature('Checkout');
        await allure.story('Multiple Item Checkout');
        await allure.severity('normal');
        await allure.tag('smoke');
        await allure.tag('regression');
        // Add three items
        await inventoryPage.addBackpackButton.click();
        await inventoryPage.addOnesieButton.click();
        await inventoryPage.addRedTshirtButton.click();

        await expect(
            inventoryPage.shoppingCartLink,
            'Cart count is not 3 after adding items'
        ).toContainText('3');

        await inventoryPage.shoppingCartLink.click();

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/cart.html'
        );

        // Cart validation
        const cartPage = new CartPage(page);

        const itemsInCart =
            await cartPage.getAllItemsDetail();

        expect(
            itemsInCart,
            `Expected 3 Items, Actually ${itemsInCart.length} items`
        ).toHaveLength(3);

        expect(itemsInCart).toEqual(
            sauceDemoData.checkout.multipleItems
        );

        // Checkout Step One
        await cartPage.clickCheckout();

        const step1Page =
            new CheckoutStepOne(page);

        await expect(step1Page.checkoutTitle)
            .toHaveText('Checkout: Your Information');

        await expect(step1Page.firstName).toBeVisible();
        await expect(step1Page.lastName).toBeVisible();
        await expect(step1Page.zipCode).toBeVisible();
        await expect(step1Page.continueBtn).toBeVisible();

        await step1Page.fillCheckoutInformation(
            sauceDemoData.checkout.customer.firstName,
            sauceDemoData.checkout.customer.lastName,
            sauceDemoData.checkout.customer.postalCode
        );

        await step1Page.clickContinue();

        // Checkout Step Two
        const step2Page =
            new CheckoutStepTwo(page);

        await expect(step2Page.finishButton).toBeVisible();
        await expect(step2Page.cancelButton).toBeVisible();

        const itemsInCheckout =
            await step2Page.getCheckoutItemsDetail();

        expect(
            itemsInCheckout,
            `Expected 3 Items, Actually ${itemsInCheckout.length} items`
        ).toHaveLength(3);

        expect(itemsInCheckout).toEqual(
            sauceDemoData.checkout.multipleItems
        );

        // Payment & Shipping validation
        const paymentInfo =
            await step2Page.getPaymentInfo();

        const shippingInfo =
            await step2Page.getShippingInfo();

        expect(
            paymentInfo,
            'Payment info mismatch'
        ).toContain(
            sauceDemoData.checkout.paymentInfo
        );

        expect(
            shippingInfo,
            'Shipping info mismatch'
        ).toBe(
            sauceDemoData.checkout.shippingInfo
        );

        // Financial summary validation
        const itemTotal =
            await step2Page.getItemTotal();

        const tax =
            await step2Page.getTax();

        const total =
            await step2Page.getTotal();

        const expectedSummary =
            sauceDemoData.checkout.multipleItemSummary;

        expect(
            itemTotal,
            'Item total mismatch'
        ).toBe(expectedSummary.itemTotal);

        expect(
            tax,
            'Tax mismatch'
        ).toBe(expectedSummary.tax);

        expect(
            total,
            'Total mismatch'
        ).toBe(expectedSummary.total);

        // Finish checkout
        await step2Page.clickFinish();

        const completePage =
            new CheckoutComplete(page);

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/checkout-complete.html'
        );

        // Checkout complete validation
        expect(
            await completePage.getCompleteTitle()
        ).toBe('Checkout: Complete!');

        expect(
            await completePage.getCompleteHeader()
        ).toBe('Thank you for your order!');

        expect(
            await completePage.getCompleteText()
        ).toBe(
            'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        );

        // Back to inventory
        await completePage.clickBackHomeBtn();

        await expect(page).toHaveURL(
            'https://www.saucedemo.com/inventory.html'
        );
    });

});