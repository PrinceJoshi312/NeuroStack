# 5. 🧩 Core Modules

### 5.1 Orchestrator (Agent Brain)

Responsible for:

* Understanding user intent
* Planning tasks
* Executing actions
* Managing tool usage

---

### 5.2 Task Planner

* Breaks user requests into steps
* Creates execution plans
* Handles retries and failures

---

### 5.3 Execution Engine

* Executes planned actions
* Interacts with tools
* Maintains execution state

---

### 5.4 Tiered Memory System

A hybrid storage architecture designed for low-latency recall and high-density long-term retention.

*   **Tier 1: Short-term Context (Redis/In-Memory):**
    *   Stores active conversation history and current execution state.
    *   **TTL Management:** Automatically expires after session inactivity (default 30 mins).
*   **Tier 2: Long-term Semantic Memory (Vector DB - ChromaDB/Pinecone):**
    *   Stores embeddings of past interactions, facts, and user preferences.
    *   **Retrieval Logic:** Top-K semantic search triggered by Orchestrator based on query intent.
    *   **Pruning Engine:** Relevance-based scoring to archive or delete low-utility vectors, preventing context window "noise."
*   **Tier 3: Relational User Store (PostgreSQL/SQLite):**
    *   Stores structured data: User profiles, global settings, and tool authentication metadata.
*   **Privacy & Control:**
    *   **Forget Command:** Natural language trigger to locate and delete specific semantic clusters.
    *   **Data Isolation:** User-specific encryption keys for vector payloads.

---

### 5.5 Sandboxed Tool Registry

A central hub for managing external integrations and executable scripts with strict isolation and permission boundaries.

*   **Execution Isolation (Sandboxing):**
    *   **External APIs:** All outgoing requests are proxied through a middleware that enforces rate limits and logs headers for auditability.
    *   **Code/Scripts:** Execution occurs in ephemeral, network-isolated environments (e.g., Docker containers or restricted Web Workers) to prevent host system access.
*   **OAuth & Scoped Permissions:**
    *   **Least Privilege:** Integrations must use the narrowest possible OAuth scopes (e.g., `calendar.events.readonly`).
    *   **Key Management:** API keys are never stored in plain text; they are retrieved from a secure secret manager and injected into the sandbox at runtime.
*   **Secure Tool Discovery:**
    *   **Manifest Verification:** Only tools with a verified `tool-manifest.json` (defining expected inputs, outputs, and required permissions) can be registered.
    *   **Human-in-the-Loop (HITL) for New Tools:** Adding or updating a tool requires a one-time manual approval from the user via the UI.
*   **Dynamic Function Calling:** Orchestrator utilizes JSON Schema-based definitions to dynamically select and invoke tools based on the Task Plan.

---
