"""
AuditAgent
----------
Responsibility:
- Observes all traffic
- Logs agent interactions for debugging and transparency
- Saves a trace.json audit trail
"""
import json
import os
from datetime import datetime
from core.agent import Agent
from core.schema import AuditLog

class AuditAgent(Agent):
    def __init__(self, name):
        super().__init__(name)
        self.logs = []

    async def think(self, message):
        print(f"DEBUG: AuditAgent logging message from {message.sender} to {message.metadata.get('original_receiver', message.receiver)}")
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "sender": message.sender,
            "receiver": message.metadata.get("original_receiver", message.receiver),
            "payload_type": type(message.payload).__name__,
            "payload": str(message.payload)[:500] # Truncated for log clarity
        }
        self.logs.append(log_entry)
        return log_entry

    async def act(self, log_entry):
        # Periodically save logs
        log_path = os.path.join(os.getcwd(), "logs")
        os.makedirs(log_path, exist_ok=True)
        file_path = os.path.join(log_path, "audit_trail.json")
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.logs, f, indent=4)
        return None
