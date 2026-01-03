"""
Message object for inter-agent communication.
Supports structured Pydantic payloads.
"""
from typing import Any, Optional

class Message:
    def __init__(self, sender: str, receiver: str, payload: Any, metadata: Optional[dict] = None):
        self.sender = sender
        self.receiver = receiver
        self.payload = payload
        self.metadata = metadata or {}
