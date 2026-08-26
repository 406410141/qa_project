import { Page } from '@playwright/test';

export class BasePage {
    constructor(protected readonly page: Page) {}

    async navigate(url: string): Promise<void> {
        await this.page.goto(url, {
            waitUntil: 'domcontentloaded',
        });
    }
}