import { Page, Locator } from '@playwright/test';
import { BasePage } from './base.page';


export class CheckoutStepOne extends BasePage{ 
    readonly checkoutTitle : Locator;
    readonly firstName : Locator;
    readonly lastName : Locator;
    readonly zipCode : Locator;
    readonly continueBtn : Locator;



    constructor(page : Page){
        super(page);
        this.checkoutTitle = page.locator('.title');
        this.firstName = page.locator('#first-name');
        this.lastName = page.locator('#last-name');
        this.zipCode = page.locator('#postal-code');
        this.continueBtn = page.locator('#continue');
    }


    async fillCheckoutInformation(firstName: string, lastName: string, zipCode: string):Promise<void>{
        await this.firstName.fill(firstName);
        await this.lastName.fill(lastName);
        await this.zipCode.fill(zipCode);
    }   
    async clickContinue(): Promise<void>{
        await this.continueBtn.click();
    }
}