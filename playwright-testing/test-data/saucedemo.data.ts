type Product = {
    id: string;
    name: string;
    price: number;
};

type ItemDetail = Omit<Product, 'id'> & {
    qty: number;
};
const data = require('../../test-data/saucedemo.json') as {
    credentials: {
        username: string;
        password: string;
        displayedUsers: string[];
    };

    products: Product[];

    checkout: {
        customer: {
            firstName: string;
            lastName: string;
            postalCode: string;
        };

        singleItemIds: string[];

        multipleItemIds: string[];

        paymentInfo: string;

        shippingInfo: string;

        singleItemSummary: {
            itemTotal: number;
            tax: number;
            total: number;
        };

        multipleItemSummary: {
            itemTotal: number;
            tax: number;
            total: number;
        };
    };

    sorting: {
        az: string[];
        za: string[];
        priceLowToHigh: number[];
        priceHighToLow: number[];
    };

    navigation: {
        menuItems: string[];
    };
};

const productsById = new Map(
    data.products.map((product) => [product.id, product])
);

function itemsFor(ids: string[]): ItemDetail[] {
    return ids.map((id) => {
        const product = productsById.get(id);

        if (!product) {
            throw new Error(
                `Unknown SauceDemo product id: ${id}`
            );
        }

        return {
            name: product.name,
            price: product.price,
            qty: 1,
        };
    });
}

export const sauceDemoData = {
    credentials: data.credentials,

    products: data.products,

    checkout: {
        ...data.checkout,

        singleItems: itemsFor(
            data.checkout.singleItemIds
        ),

        multipleItems: itemsFor(
            data.checkout.multipleItemIds
        ),
    },

    sorting: data.sorting,

    navigation: data.navigation,
};