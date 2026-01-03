"""
DataValidationAgent (Async)
"""
from core.agent import Agent
from core.message import Message

class DataValidationAgent(Agent):
    REQUIRED_FIELDS = [
        "Product Name", "Concentration", "Skin Type", 
        "Key Ingredients", "Benefits", "How to Use", 
        "Side Effects", "Price"
    ]

    async def think(self, message):
        data = message.payload
        missing = [f for f in self.REQUIRED_FIELDS if f not in data or not data[f]]
        
        if missing:
            return {"valid": False, "error": f"Missing: {missing}"}
        return {"valid": True, "data": data}

    async def act(self, result):
        if not result["valid"]:
            return Message(sender=self.name, receiver="OutputAgent", payload=result)
        
        return Message(
            sender=self.name,
            receiver="ParserAgent",
            payload=result["data"]
        )
