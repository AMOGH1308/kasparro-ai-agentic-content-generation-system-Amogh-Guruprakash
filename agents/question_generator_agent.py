from genai_client import client
from google.genai import types
from logic_blocks.question_logic import categorize_questions

class QuestionGeneratorAgent:
    def run(self, product):
        prompt = f"""
Generate 20 diverse user questions about the following product.
Return ONLY the questions, one per line, no numbering.

Product:
{product}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(max_output_tokens=400)
        )

        questions = [
            q.strip("-• ").strip()
            for q in response.text.split("\n")
            if q.strip()
        ]

        return categorize_questions(questions)
