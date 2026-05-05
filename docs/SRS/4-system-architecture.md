# 4. 🧱 System Architecture

### High-Level Architecture

```
Client Layer (UI)
   ├── Chat Interface (with Action Logs & HITL Prompts)
   ├── Voice Interface
   └── Dashboard

        ↓

Safety & Governance Layer (Guardrails)
   ├── Token/Budget Monitor
   ├── HITL Manager
   ├── Policy Enforcer

        ↓

Orchestrator Layer (Agent Brain)
   ├── Task Planner (Hierarchical)
   ├── Execution Engine (Stateful)
   ├── Tool Router (OAuth Scoped)

        ↓

LLM Layer
   ├── Gemini API (Primary Reasoning)
   ├── Optional Local LLM (Ollama - Specialized Tasks)

        ↓

Memory Layer
   ├── Short-term Memory (Redis/In-memory)
   ├── Long-term Memory (Vector DB with Pruning Logic)
   ├── User Preference Store (Relational)

        ↓

Tool Layer (Sandboxed)
   ├── APIs (Email, Calendar, etc.)
   ├── Browser Automation (Playwright/Puppeteer)
   ├── Smart Home Integrations

        ↓

Storage Layer
   ├── PostgreSQL / SQLite (System State & User Data)
   ├── ChromaDB / Pinecone (Embeddings)
```

---
