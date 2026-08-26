import { Page, Locator } from '@playwright/test';
import { BasePage } from './base.page';


export class CheckoutComplete extends BasePage{
    readonly completeTitle : Locator;
    readonly completeHeader : Locator;    
    readonly completeText : Locator;
    readonly backHomeBtn : Locator;
    

    constructor(page : Page){
        super(page);
        this.completeTitle = page.locator('.title');
        this.completeHeader = page.locator('.complete-header');
        this.completeText = page.locator('.complete-text');
        this.backHomeBtn = page.locator('#back-to-products')
    }
    async getCompleteTitle(): Promise<string> {
        return await this.completeTitle.innerText();
    }
    async getCompleteHeader(): Promise<string> {
        return await this.completeHeader.innerText();
    }
    async getCompleteText(): Promise<string> {
        return await this.completeText.innerText();
    }   

    async clickBackHomeBtn(): Promise<void> {
        await this.backHomeBtn.click();
    }




}