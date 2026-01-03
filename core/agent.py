"""
Base Agent class (Async).
"""
from core.message import Message

class Agent:
    def __init__(self, name: str):
        self.name = name
        self.inbox = []

    async def receive(self, message: Message):
        self.inbox.append(message)

    async def think(self, message: Message):
        raise NotImplementedError

    async def act(self, result) -> Message:
        raise NotImplementedError
