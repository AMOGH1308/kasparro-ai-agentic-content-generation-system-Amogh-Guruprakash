def compare_products(a, b):
    return {
        "product_a": a["name"],
        "product_b": b["name"],
        "ingredient_comparison": f"{a['ingredients']} vs {b['ingredients']}",
        "benefits_comparison": f"{a['benefits']} vs {b['benefits']}",
        "price_comparison": f"{a['price']} vs {b['price']}"
    }
