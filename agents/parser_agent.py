"""
ParserAgent (Async + Pydantic)
"""
from core.agent import Agent
from core.message import Message
from core.schema import ProductData

class ParserAgent(Agent):
    async def think(self, message):
        raw = message.payload
        # Instantiate Pydantic model for validation
        return ProductData(
            name=raw["Product Name"],
            concentration=raw["Concentration"],
            skin_type=raw["Skin Type"],
            ingredients=raw["Key Ingredients"],
            benefits=raw["Benefits"],
            usage=raw["How to Use"],
            side_effects=raw["Side Effects"],
            price=raw["Price"]
        )

    async def act(self, parsed_product: ProductData):
        return Message(
            sender=self.name,
            receiver="QuestionAgent",
            payload=parsed_product
        )
