"""
OutputAgent (Async)
"""
import json
import os
import shutil
from core.agent import Agent

class OutputAgent(Agent):
    async def think(self, message):
        return message.payload

    async def act(self, result):
        if not isinstance(result, dict):
            print(f"ERROR: Expected dict in OutputAgent, got {type(result)}")
            return None

        # Fresh output dir
        if os.path.exists("output"):
            shutil.rmtree("output")
        os.makedirs("output", exist_ok=True)

        for page_name, content in result.items():
            if page_name == "valid": continue # Skip validation results
            file_path = os.path.join("output", f"{page_name}.json")
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(content, f, indent=4, ensure_ascii=False)
            print(f"Saved: {file_path}")

        print("\n===== SYSTEM TASK COMPLETE =====")
        return None
