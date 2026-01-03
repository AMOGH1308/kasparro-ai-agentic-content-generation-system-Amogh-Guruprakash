"""
Advanced Agentic System Entry Point (Async)
"""
import asyncio
import json
import os

from core.orchestrator import Orchestrator
from core.message import Message

from agents.input_agent import InputAgent
from agents.data_validation_agent import DataValidationAgent
from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionAgent
from agents.editor_agent import EditorAgent
from agents.template_agent import TemplateAgent
from agents.output_agent import OutputAgent
from agents.audit_agent import AuditAgent

async def main():
    # Load raw product data
    data_path = os.path.join("data", "product.json")
    with open(data_path, "r", encoding="utf-8") as f:
        raw_product = json.load(f)

    orchestrator = Orchestrator()

    # Register all agents including new ones
    orchestrator.register(AuditAgent("AuditAgent")) # Observability
    orchestrator.register(InputAgent("InputAgent"))
    orchestrator.register(DataValidationAgent("DataValidationAgent"))
    orchestrator.register(ParserAgent("ParserAgent"))
    orchestrator.register(QuestionAgent("QuestionAgent"))
    orchestrator.register(EditorAgent("EditorAgent")) # Quality Control Loop
    orchestrator.register(TemplateAgent("TemplateAgent"))
    orchestrator.register(OutputAgent("OutputAgent"))

    print("--- Starting Advanced Agentic System ---")
    start_message = Message(
        sender="SYSTEM",
        receiver="InputAgent",
        payload=raw_product
    )

    await orchestrator.start(start_message)

if __name__ == "__main__":
    asyncio.run(main())
