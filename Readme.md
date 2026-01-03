# Kasparro AI: Agentic Content Generation System

- **Advanced Agentic Logic**: Multi-agent message-passing architecture.
- **Automated Quality**: High-fidelity content generation via self-correction loops.
- **Async Engine**: High-performance concurrently-processed workflows.

## 🚀 Quick Start

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AMOGH1308/kasparro-ai-agentic-content-generation-system-Amogh-Guruprakash.git
   cd kasparro-ai-agentic-content-generation-system-Amogh-Guruprakash
   ```

2. **Configure Virtual Environment**:
- **Isolation**: Prevents dependency conflicts.
- **Consistency**: Ensures a reproducible environment.
   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate it (Windows)
   .\venv\Scripts\activate

   # Activate it (macOS/Linux)
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**:
   - Open the `.env` file in the root directory.
   - Replace `enter_api_key_over_here` with your valid Google Gemini API Key.
   - *Note: If no key is provided, the system will automatically fall back to a sophisticated mock generation mode.*

5. **Run the System**:
   ```bash
   python main.py
   ```

## 📂 Project Structure

- `main.py`: Entry point for the async orchestrator.
- `core/`: Base agent classes, message routing, and Pydantic schemas.
- `agents/`: Specialized autonomous agents (Validation, Parser, AI-Generation, Editor/Critique).
- `data/`: Input product data.
- `templates/`: Structured JSON output templates.
- `output/`: Final machine-readable content pages.
- `logs/`: Complete execution audit trails.

## ✨ Key Architectural Features

### 1. The Message-Bus Orchestrator
- **Message Decoupling**: Agents communicate via center-hub routing.
- **Concurrency**: `asyncio` loop prevents I/O-bound blocking.
- **Flexibility**: No hard-coded function dependencies between agents.

### 2. The "Editor-in-the-Loop" (Self-Correction)
- **Quality Gating**: Heuristic-based review of AI-generated content.
- **Feedback Loops**: Autonomous critique-regeneration cycles.
- **Refinement**: Ensures high-fidelity output without human intervention.

### 3. Strict Data Contracts (Pydantic)
- **Error Prevention**: Validates data structures at every handoff point.
- **Contract Enforcement**: Enforced schemas for all inter-agent messages.
- **Integrity**: Guarantees content compatibility with hydration templates.

## 📄 Detailed Documentation
- **Flow Control**: State Machine & Sequence Diagrams.
- **Schema Mapping**: Class diagrams and logic block definitions.
- **Detailed Design**: [docs/projectdocumentation.md](docs/projectdocumentation.md)
