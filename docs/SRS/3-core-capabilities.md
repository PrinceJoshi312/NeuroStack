# 3. ⚙️ Core Capabilities

### 3.1 Baseline Features (Parity with Assistants)

* Voice commands
* Reminders, alarms, scheduling
* Weather and quick queries
* Media playback
* Messaging and calling
* Smart home control

---

### 3.2 Advanced LLM Capabilities (Differentiator)

* **Multi-step Reasoning & Planning:** Hierarchical planning with step-by-step verification.
* **Secured Tool Usage:** OAuth-driven integration with scoped permissions and environment variable isolation.
* **Tiered Memory System:** Hybrid approach using session context (short-term) and semantic retrieval (long-term) with active pruning.
* **Context-Aware Safety Guardrails:** 
    * **Kill-switch:** Immediate termination of all active background processes.
    * **Human-in-the-Loop (HITL):** Mandatory confirmation for high-stakes actions (e.g., deleting data, financial transactions, sending external communications).
    * **Budget Caps:** User-defined limits on API tokens and execution time per task.
* **Autonomous Task Execution:** Execution within "sandboxed" environments for browser and code tasks to prevent system-level damage.
* **Cross-application Workflows:** Orchestration across multiple authenticated services with state rollback on failure.

---
