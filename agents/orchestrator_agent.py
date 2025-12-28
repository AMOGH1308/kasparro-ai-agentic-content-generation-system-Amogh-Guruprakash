import json

from agents.input_parser_agent import InputParserAgent
from agents.question_generator_agent import QuestionGeneratorAgent
from agents.template_engine_agent import TemplateEngineAgent

from logic_blocks.comparison_logic import compare_products


class OrchestratorAgent:
    def __init__(self):
        self.parser = InputParserAgent()
        self.questioner = QuestionGeneratorAgent()
        self.template_engine = TemplateEngineAgent()

    def run(self, raw_data):
        # Parse product
        parsed = self.parser.run(raw_data)

        # Generate categorized questions
        categorized_questions = self.questioner.run(parsed)

        # Fictional Product B
        product_b = {
            "name": "RadiantGlow Serum B",
            "ingredients": "Vitamin E, Green Tea Extract",
            "benefits": "Hydration, Oil Control",
            "price": "₹899"
        }

        # Comparison logic
        comparison_data = compare_products(parsed, product_b)

        # Apply templates
        faq_json = self.template_engine.apply_template(
            "faq_template.json",
            {
                "product": parsed["name"],
                "questions": categorized_questions
            }
        )

        product_json = self.template_engine.apply_template(
            "product_template.json",
            parsed
        )

        comparison_json = self.template_engine.apply_template(
            "comparison_template.json",
            comparison_data
        )

        # Save output files
        with open("output/faq.json", "w") as f:
            json.dump(faq_json, f, indent=4)

        with open("output/product_page.json", "w") as f:
            json.dump(product_json, f, indent=4)

        with open("output/comparison_page.json", "w") as f:
            json.dump(comparison_json, f, indent=4)

        return {
            "faq": faq_json,
            "product_page": product_json,
            "comparison_page": comparison_json
        }
