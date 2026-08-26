import { Page, Locator } from '@playwright/test';
import { BasePage } from './base.page';

export class CartPage extends BasePage {
    readonly continueShoppingButton: Locator;
    readonly checkoutButton: Locator;
    readonly cartTitle: Locator;
    readonly cartItemContainer: Locator;

    constructor(page: Page) {
        super(page);
        this.continueShoppingButton = page.locator('#continue-shopping');
        this.checkoutButton = page.locator('#checkout');
        this.cartTitle = page.locator("[data-test='title']");
        this.cartItemContainer = page.locator('.cart_item');
    }

    async getAllItemsDetail(): Promise<{ name: string; price: number; qty: number }[]> {
        const count = await this.cartItemContainer.count();
        const itemDetails = [];

        for (let i = 0; i < count; i++) {
            const item = this.cartItemContainer.nth(i);
            const name = await item.locator('.inventory_item_name').innerText();
            const priceRaw = await item.locator('.inventory_item_price').innerText();
            const qty = await item.locator('.cart_quantity').innerText();

            itemDetails.push({
                name,
                price: parseFloat(priceRaw.replace('$', '')),
                qty: parseInt(qty, 10),
            });
        }

        return itemDetails;
    }

    async clickContinueShopping(): Promise<void> {
        await this.continueShoppingButton.click();
    }

    async clickCheckout(): Promise<void> {
        await this.checkoutButton.click();
    }
}