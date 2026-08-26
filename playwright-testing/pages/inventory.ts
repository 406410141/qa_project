import { Page, Locator } from '@playwright/test';
import { BasePage } from './base.page';

export class InventoryPage extends BasePage {

  readonly sideMenuButton: Locator;
  readonly sidebarContainer: Locator;
  readonly allItemsLink: Locator;
  readonly aboutLink: Locator;
  readonly logoutLink: Locator;
  readonly resetLink: Locator;
  readonly closeSidebarButton: Locator;

  readonly shoppingCartLink: Locator;
  readonly shoppingCartBadge: Locator;

  readonly addBackpackButton: Locator;
  readonly addOnesieButton: Locator;
  readonly addRedTshirtButton: Locator;

  readonly inventoryList: Locator;
  readonly itemNames: Locator;
  readonly itemPrices: Locator;
  readonly sortSelect: Locator;

  constructor(page: Page) {
    super(page);


    this.sideMenuButton = page.locator('#react-burger-menu-btn');
    this.sidebarContainer = page.locator('.bm-menu-wrap');
    this.allItemsLink = page.locator('#inventory_sidebar_link');
    this.aboutLink = page.locator('#about_sidebar_link');
    this.logoutLink = page.locator('#logout_sidebar_link');
    this.resetLink = page.locator('#reset_sidebar_link');
    this.closeSidebarButton = page.locator('#react-burger-cross-btn');


    this.shoppingCartLink = page.locator('.shopping_cart_link');
    this.shoppingCartBadge = page.locator('.shopping_cart_badge');


    this.addBackpackButton = page.locator('#add-to-cart-sauce-labs-backpack');
    this.addOnesieButton = page.locator('#add-to-cart-sauce-labs-onesie');
    this.addRedTshirtButton = page.locator('[id="add-to-cart-test.allthethings()-t-shirt-(red)"]');


    this.inventoryList = page.locator('.inventory_list');
    this.itemNames = page.locator('.inventory_item_name');
    this.itemPrices = page.locator('.inventory_item_price');
    this.sortSelect = page.locator('.product_sort_container');
  }


  async openSideMenu(): Promise<void> {
    await this.sideMenuButton.click();
  }

  async closeSideMenu(): Promise<void> {
    await this.closeSidebarButton.click();
  }

  async clickLogout(): Promise<void> {
    await this.logoutLink.click();
  }

  async clickShoppingCart(): Promise<void> {
    await this.shoppingCartLink.click();
  }


  async isSidebarHidden(): Promise<boolean> {
    const status = await this.sidebarContainer.getAttribute('aria-hidden');
    return status === 'true';
  }


  async getAllItemNames(): Promise<string[]> {
    const items = await this.itemNames.allTextContents();
    return items.map(item => item.trim());
  }


  async getAllItemPrices(): Promise<number[]> {
    const items = await this.itemPrices.allTextContents();
    return items.map(item => parseFloat(item.replace('$', '').trim()));
  }


  async sortBy(optionValue: 'az' | 'za' | 'lohi' | 'hilo'): Promise<void> {
    await this.sortSelect.selectOption(optionValue);
  }
}