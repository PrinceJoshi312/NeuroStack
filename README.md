# AgentOS 🧠

AgentOS is a next-generation AI assistant platform designed to go beyond traditional voice assistants. It executes multi-step tasks autonomously, integrates dynamically with tools, and maintains a tiered memory system for deep personalization.

## 🚀 Key Features

- **Hierarchical Planning:** Multi-step reasoning with step-by-step verification.
- **Safety Guardrails:** Hard kill-switches, budget caps, and Human-in-the-Loop (HITL) confirmations.
- **Tiered Memory System:** Hybrid architecture using Redis (short-term) and Vector DBs (long-term) with active pruning.
- **Sandboxed Tool Registry:** Execution of tools and scripts in isolated environments with scoped OAuth permissions.

## 📂 Project Structure

```text
agentos/
├── backend/            # FastAPI Backend
│   └── app/
│       ├── api/        # REST Endpoints
│       ├── agents/     # Orchestrator & Planning logic
│       ├── tools/      # Sandboxed Tool Registry
│       ├── memory/     # Tiered Memory Logic
│       ├── services/   # External Integrations
│       └── core/       # Config & Security
├── frontend/           # React Frontend
├── worker/             # Background Task Runner
├── docs/               # Sharded SRS and Architecture docs
└── scripts/            # Utility scripts
```

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python
- **Frontend:** React, TypeScript
- **Database:** SQLite (Relational), Redis (Cache), ChromaDB (Vector)
- **LLM:** Gemini API (Primary), Ollama (Local/Specialized)

## 🏗️ Getting Started

*(Instructions for setting up the local environment and Phase 1 MVP will be added here.)*

---

## 📄 Documentation

The project documentation is sharded for clarity:
- [System Architecture](./docs/SRS/4-system-architecture.md)
- [Core Modules](./docs/SRS/5-core-modules.md)
- [Safety & Security](./docs/SRS/8-security-privacy.md)
- [Development Roadmap](./docs/SRS/7-development-roadmap.md)
