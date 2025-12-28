def parse_product_data(raw):
    return {
        "name": raw.get("Product Name"),
        "concentration": raw.get("Concentration"),
        "skin_type": raw.get("Skin Type"),
        "ingredients": raw.get("Key Ingredients"),
        "benefits": raw.get("Benefits"),
        "usage": raw.get("How to Use"),
        "side_effects": raw.get("Side Effects"),
        "price": raw.get("Price")
    }
