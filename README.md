# LangGraph & LangSmith — From Zero to Expert

A hands-on learning repository: 18 steps across 6 phases, from basic
LangSmith tracing to multi-agent architectures with long-term memory
and production-grade guardrails.

## Stack
- Python 3.12
- [LangGraph](https://langchain-ai.github.io/langgraph/)
- [LangSmith](https://smith.langchain.com/)
- Dependency manager: [uv](https://docs.astral.sh/uv/)

## Structure
Each phase is a folder; each step within a phase is a standalone
executable `main.py` script.

## Setup
\`\`\`bash
uv sync
cp .env.example .env  # fill in your API keys
uv run python phase-1-observability/step-1-basic-tracing/main.py
\`\`\`

## Progress

| Step | Description | Status |
|---|---|---|
| 1 | Basic Tracing & Configuration | 🚧 |
| 2 | Chain Tracing (LCEL) | ⬜ |
| 3 | Metadata & Tags | ⬜ |
| 4 | Linear Graph (State, nodes, edges) | ⬜ |
| ... | ... | ⬜ |

## Note
Use cases are generically inspired by domains like fintech and
conversational assistants, for educational purposes only.
