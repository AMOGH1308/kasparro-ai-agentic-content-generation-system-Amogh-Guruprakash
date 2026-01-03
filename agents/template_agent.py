"""
TemplateAgent (Async + Pydantic)
"""
import json
import os
from core.agent import Agent
from core.message import Message
from core.schema import QuestionOutput

class TemplateAgent(Agent):
    async def think(self, message):
        data: QuestionOutput = message.payload
        product = data.product.dict()
        questions = data.questions.dict()
        prod_b = data.product_b.dict()

        def load_tpl(name):
            path = os.path.join("templates", name)
            if not os.path.exists(path):
                return {}
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)

        # FAQ Page
        faq_tpl = load_tpl("faq.json")
        faq_tpl["title"] = faq_tpl.get("title", "").replace("{product_name}", product["name"])
        faq_tpl["questions"] = questions

        # Product Page
        prod_tpl = load_tpl("product.json")
        prod_tpl.update({
            "name": product["name"],
            "concentration": product["concentration"],
            "skin_type": product["skin_type"],
            "key_ingredients": product["ingredients"],
            "benefits": product["benefits"],
            "how_to_use": product["usage"],
            "side_effects": product["side_effects"],
            "price": product["price"]
        })

        # Comparison Page
        comp_tpl = load_tpl("comparison.json")
        comp_tpl["product_a"] = {
            "name": product["name"],
            "ingredients": product["ingredients"],
            "benefits": product["benefits"],
            "price": product["price"]
        }
        comp_tpl["product_b"] = prod_b
        comp_tpl["comparison_summary"] = {
            "ingredients_comparison": f"{product['name']} vs {prod_b['name']}",
            "benefits_comparison": f"High potency vs {prod_b['benefits']}",
            "price_comparison": f"{product['price']} vs {prod_b['price']}"
        }

        return {
            "faq_page": faq_tpl,
            "product_page": prod_tpl,
            "comparison_page": comp_tpl
        }

    async def act(self, content):
        return Message(
            sender=self.name,
            receiver="OutputAgent",
            payload=content
        )
