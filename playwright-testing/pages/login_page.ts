import { Page, Locator } from '@playwright/test';
import { BasePage } from './base.page';

export class LoginPage extends BasePage {
    readonly url = 'https://www.saucedemo.com/';

    readonly usernameInput: Locator;
    readonly passwordInput: Locator;
    readonly loginButton: Locator;
    readonly errorContainer: Locator;
    readonly closeErrorButton: Locator;

    readonly logo: Locator;
    readonly allUsernames: Locator;
    readonly allPassword: Locator;

    readonly acceptedUsername = 'standard_user';
    readonly acceptedPassword = 'secret_sauce';

    constructor(page: Page) {
        super(page);
        this.usernameInput = page.locator('#user-name');
        this.passwordInput = page.locator('#password');
        this.loginButton = page.locator('#login-button');
        this.errorContainer = page.locator('[data-test="error"]');
        this.closeErrorButton = page.locator('.error-button');

        this.logo = page.locator('.login_logo');
        this.allUsernames = page.locator('#login_credentials');
        this.allPassword = page.locator('.login_password');
    }
    async goto(): Promise<void> {
        await this.navigate(this.url);
    }

    async login(username: string, password: string): Promise<void> {
        await this.usernameInput.fill(username);
        await this.passwordInput.fill(password);
        await this.loginButton.click();
    }

    async getErrorMessage(): Promise<string> {
        return await this.errorContainer.innerText();
    }


    async clickErrorButton(): Promise<void> {
        await this.closeErrorButton.click();
    }
}