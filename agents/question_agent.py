"""
QuestionAgent (Async + Pydantic + Retry Support)
"""
import os
import json
import asyncio
import warnings
from typing import Optional

# Suppress warnings from deprecated google-generativeai package
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from dotenv import load_dotenv

from core.agent import Agent
from core.message import Message
from core.schema import ProductData, QuestionOutput, FAQData, ProductBData

class QuestionAgent(Agent):
    async def think(self, message):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        
        # Handle different payload types (Initial vs Retry)
        if isinstance(message.payload, ProductData):
            product = message.payload
            critique = None
            iteration = 1
        else:
            # Re-generation request from EditorAgent
            product = message.payload.product
            critique = message.payload.critique
            iteration = message.payload.iteration

        if not api_key or api_key == "enter_api_key_over_here":
            mock_data = self._generate_mock_faq_and_competitor(product)
            return QuestionOutput(
                product=product,
                product_b=ProductBData(**mock_data["product_b"]),
                questions=FAQData(**mock_data["faq"]),
                iteration=iteration
            )

        # List of models to try
        models_to_try = [
            'models/gemini-flash-latest',
            'models/gemini-1.5-flash',
            'models/gemini-2.0-flash-exp'
        ]

        last_error = None
        for model_name in models_to_try:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_name)
                
                critique_context = f"\nPREVIOUS CRITIQUE: {critique}\nPlease address these issues specifically." if critique else ""
                
                prompt = f"""
                Identify as a product specialist. Generate a detailed FAQ and a fictional competitor (Product B) for:
                {product.json()}
                {critique_context}

                REQUIREMENTS:
                1. FAQ CATEGORIES: Informational, Usage, Safety, Purchase, Comparison.
                2. VOLUME: At least 15 unique, high-quality Q&As.
                3. PRODUCT B: Must be the EXACT same category but strategically different.
                
                OUTPUT FORMAT: Return ONLY a raw JSON object. No markdown.
                {{
                    "faq": {{
                        "Informational": [{{"q": "...", "a": "..."}}, ...],
                        "Usage": [...],
                        "Safety": [...],
                        "Purchase": [...],
                        "Comparison": [...]
                    }},
                    "product_b": {{
                        "name": "...",
                        "ingredients": "...",
                        "benefits": "...",
                        "price": "..."
                    }}
                }}
                """

                loop = asyncio.get_event_loop()
                response = await loop.run_in_executor(None, lambda: model.generate_content(prompt))
                
                text = response.text.strip()
                # Extraction logic for JSON
                if "```" in text:
                    if "```json" in text:
                        text = text.split("```json")[1].split("```")[0].strip()
                    else:
                        text = text.split("```")[1].split("```")[0].strip()
                
                data = json.loads(text)
                return QuestionOutput(
                    product=product,
                    product_b=ProductBData(**data["product_b"]),
                    questions=FAQData(**data["faq"]),
                    iteration=iteration
                )
            except Exception as e:
                last_error = e
                continue

        print(f"All Gemini models failed. Last error: {last_error}. Falling back to Mock.")
        mock_data = self._generate_mock_faq_and_competitor(product)
        return QuestionOutput(
            product=product,
            product_b=ProductBData(**mock_data["product_b"]),
            questions=FAQData(**mock_data["faq"]),
            iteration=iteration
        )

    def _generate_mock_faq_and_competitor(self, product):
        name = product.name
        return {
            "product_b": {
                "name": f"EliteGlow Serum B",
                "ingredients": "Glycerin, Vitamin E, Synthetic Actives",
                "benefits": "Deep hydration and basic barrier protection",
                "price": "₹899"
            },
            "faq": {
                "Informational": [
                    {"q": f"How does {name} support skin barrier health?", "a": "It uses balanced actives to protect the lipid layer."},
                    {"q": f"Is {name} suitable for sensitive skin?", "a": "Yes, it is dermatologically tested for all skin types."},
                    {"q": f"What is the source of the {product.ingredients} in {name}?", "a": "Our ingredients are ethically sourced and medical-grade."}
                ],
                "Usage": [
                    {"q": f"Can I use {name} with Retinol?", "a": "Yes, but we recommend alternating nights to avoid sensitivity."},
                    {"q": f"How many drops of {name} should I apply?", "a": "2-3 drops are sufficient for the entire face."},
                    {"q": f"Can I apply makeup over {name}?", "a": "Yes, wait 60 seconds for full absorption first."}
                ],
                "Safety": [
                    {"q": f"Is {name} safe for pregnancy?", "a": "Consult your doctor; ingredients are generally safe but medical advice is best."},
                    {"q": f"Will {name} cause purging?", "a": "Minor purging can occur as cell turnover increases, usually lasting 1 week."},
                    {"q": f"Is {name} non-comedogenic?", "a": "Yes, it is formulated to not clog pores."}
                ],
                "Purchase": [
                    {"q": "Is the packaging recyclable?", "a": "Yes, we use 100% recyclable glass and minimal plastic."},
                    {"q": f"Where is {name} manufactured?", "a": "It is produced in our ISO-certified cleanroom facility."},
                    {"q": "Do you offer a subscription discount?", "a": "Yes, subscribers save 15% on every order."}
                ],
                "Comparison": [
                    {"q": f"How is {name} better than Competitor B?", "a": "It features a higher concentration of stabilized actives."},
                    {"q": f"Does {name} replace my moisturizer?", "a": "It is a treatment serum; we recommend following with moisturizer."},
                    {"q": f"Is {name} more effective than drug-store alternatives?", "a": "Yes, due to its medical-grade purity and delivery system."}
                ]
            }
        }

    async def act(self, payload: QuestionOutput):
        return Message(
            sender=self.name,
            receiver="EditorAgent",
            payload=payload
        )
