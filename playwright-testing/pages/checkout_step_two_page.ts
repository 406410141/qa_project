import { Page, Locator } from '@playwright/test';
import { BasePage } from './base.page';

export class CheckoutStepTwo extends BasePage {
    // Locators
    readonly checkoutTitle: Locator;
    readonly cartItem: Locator;
    // Amounts
    readonly itemTotal: Locator;
    readonly tax: Locator;
    readonly total: Locator;
    // Payment / Shipping Info
    readonly paymentValue: Locator;
    readonly shippingValue: Locator;
    // Finish button
    readonly finishButton: Locator;
    readonly cancelButton : Locator;
 
    constructor(page: Page) {
        super(page);
        this.checkoutTitle = page.locator('.title');
        this.cartItem = page.locator('.cart_item');
        this.itemTotal = page.locator('.summary_subtotal_label');
        this.tax = page.locator('.summary_tax_label');
        this.total = page.locator('.summary_total_label');
        this.paymentValue = page.locator('[data-test="payment-info-value"]');
        this.shippingValue = page.locator('[data-test="shipping-info-value"]');
        this.finishButton = page.locator('#finish');
        this.cancelButton = page.locator('#cancel');
    }

    async getCheckoutItemsDetail(): Promise<{ name: string; price: number; qty: number }[]> {
        const items = await this.cartItem.all();
        return Promise.all(
            items.map(async (item) => {
                const name = await item.locator('.inventory_item_name').innerText();
                const priceRaw = await item.locator('.inventory_item_price').innerText();
                const qty = await item.locator('.cart_quantity').innerText();
                return {
                    name: name.trim(),
                    price: parseFloat(priceRaw.replace('$', '')),
                    qty: parseInt(qty, 10),
                };
            })
        );
    }

    async getItemTotal(): Promise<number> {
        const text = await this.itemTotal.innerText();
        return Number(text.replace('Item total: $', ''));
    }

    async getTax(): Promise<number> {
        const text = await this.tax.innerText();
        return Number(text.replace('Tax: $', ''));
    }

    async getTotal(): Promise<number> {
        const text = await this.total.innerText();
        return Number(text.replace('Total: $', ''));
    }

    async getPaymentInfo(): Promise<string> {
        return await this.paymentValue.innerText();
    }

    async getShippingInfo(): Promise<string> {
        return await this.shippingValue.innerText();
    }

    async clickFinish(): Promise<void> {
        await this.finishButton.click();
    }
}