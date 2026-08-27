import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parents[1] / "test-data" / "saucedemo.json"

with DATA_FILE.open(encoding="utf-8") as file:
    SAUCEDEMO_DATA = json.load(file)


def item_details(product_ids):
    products_by_id = {
        product["id"]: product for product in SAUCEDEMO_DATA["products"]
    }
    return [
        {
            "name": products_by_id[product_id]["name"],
            "price": products_by_id[product_id]["price"],
            "qty": 1,
        }
        for product_id in product_ids
    ]
