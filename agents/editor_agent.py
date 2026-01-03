"""
EditorAgent
-----------
Responsibility:
- Critiques the output of QuestionAgent
- Checks for depth, categorization, and quality
- Forces a retry loop if standards aren't met
"""
from core.agent import Agent
from core.message import Message
from core.schema import QuestionOutput

class EditorAgent(Agent):
    async def think(self, message):
        data: QuestionOutput = message.payload
        
        # Logic: We want at least 3 questions in 'Safety' and 'Comparison'
        # and a minimum of 15 questions total.
        total_questions = (
            len(data.questions.Informational) +
            len(data.questions.Usage) +
            len(data.questions.Safety) +
            len(data.questions.Purchase) +
            len(data.questions.Comparison)
        )

        critique = []
        if total_questions < 15:
            critique.append(f"Insufficient quantity: Only {total_questions} questions generated. Need at least 15.")
        
        if len(data.questions.Safety) < 2:
            critique.append("Safety section is too sparse. Add more depth regarding side effects or contraindications.")

        if "B" in data.product_b.name.upper() and len(data.product_b.benefits) < 20:
             critique.append("Competitor Product B description is too generic. Make it more distinct.")

        if critique and data.iteration < 3: # Limit retries to 3
            data.critique = " | ".join(critique)
            data.iteration += 1
            return {"status": "REJECTED", "data": data}
        
        return {"status": "APPROVED", "data": data}

    async def act(self, result):
        if result["status"] == "REJECTED":
            print(f"DEBUG: EditorAgent REJECTED content (Iteration {result['data'].iteration}). Sending back...")
            return Message(
                sender=self.name,
                receiver="QuestionAgent",
                payload=result["data"]
            )
        
        return Message(
            sender=self.name,
            receiver="TemplateAgent",
            payload=result["data"]
        )
