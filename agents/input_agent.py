"""
InputAgent (Async)
"""
from core.agent import Agent
from core.message import Message

class InputAgent(Agent):
    async def think(self, message):
        return message.payload

    async def act(self, raw_input):
        return Message(
            sender=self.name,
            receiver="DataValidationAgent",
            payload=raw_input
        )
