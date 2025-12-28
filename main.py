import json
from agents.orchestrator_agent import OrchestratorAgent


def load_dynamic_data():
    """
    Loads product data dynamically from data/product.json.
    If not found, fallback to test data.
    """
    try:
        with open("data/product.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠ No dynamic product.json found — using fallback test data.")
        return {
            "Product Name": "GlowBoost Vitamin C Serum",
            "Concentration": "10% Vitamin C",
            "Skin Type": "Oily, Combination",
            "Key Ingredients": "Vitamin C, Hyaluronic Acid",
            "Benefits": "Brightening, Fades dark spots",
            "How to Use": "Apply 2–3 drops in the morning before sunscreen",
            "Side Effects": "Mild tingling for sensitive skin",
            "Price": "₹699"
        }


if __name__ == "__main__":
    orchestrator = OrchestratorAgent()
    product_data = load_dynamic_data()
    output = orchestrator.run(product_data)
    print("Generated Output:", output)
