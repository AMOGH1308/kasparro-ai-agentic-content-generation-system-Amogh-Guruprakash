"""
Async Orchestrator = message router with Observability.
Processes agents concurrently.
"""
import asyncio
from core.message import Message

class Orchestrator:
    def __init__(self):
        self.agents = {}
        self.queue = asyncio.Queue()

    def register(self, agent):
        self.agents[agent.name] = agent

    async def route(self, message: Message):
        # Every message is also sent to the AuditAgent if it exists
        if "AuditAgent" in self.agents and message.receiver != "AuditAgent":
            audit_msg = Message(
                sender=message.sender,
                receiver="AuditAgent",
                payload=message.payload,
                metadata={"original_receiver": message.receiver}
            )
            await self.agents["AuditAgent"].receive(audit_msg)
            await self.queue.put("AuditAgent")

        receiver = self.agents.get(message.receiver)
        if receiver:
            await receiver.receive(message)
            await self.queue.put(message.receiver)

    async def start(self, initial_message: Message):
        await self.route(initial_message)

        while True:
            # Check if all agents are idle and queue is empty
            if self.queue.empty():
                # Allow a small grace period for async tasks to register
                await asyncio.sleep(0.5)
                if self.queue.empty():
                    break

            agent_name = await self.queue.get()
            agent = self.agents[agent_name]
            
            if agent.inbox:
                msg = agent.inbox.pop(0)
                # Agents think and act concurrently
                result = await agent.think(msg)
                outgoing = await agent.act(result)
                if outgoing:
                    if isinstance(outgoing, list):
                        for m in outgoing:
                            await self.route(m)
                    else:
                        await self.route(outgoing)
            
            self.queue.task_done()
