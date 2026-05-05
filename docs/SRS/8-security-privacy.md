# 8. 🔐 Security & Privacy

### 8.1 Data Protection
* **Encryption:** API keys and sensitive credentials stored using AES-256 (Fernet) with user-managed keys where applicable.
* **Isolation:** Multi-tenant architecture (even for local-first) to ensure strict user data isolation.
* **Pruning & Right to be Forgotten:** Automated routines for clearing session memory and user-initiated "Forget" commands to prune specific vectors from the Vector DB.

### 8.2 Execution Security
* **Prompt Injection Mitigation:** Use of system-level delimiters and secondary "checker" LLM calls to validate agent-generated plans before execution.
* **Sandbox Isolation:** Browser automation and code execution performed in containerized or ephemeral environments (e.g., Docker/Web Workers) with restricted network access.
* **OAuth Scoping:** Tools must request the "Principle of Least Privilege" scopes (e.g., `gmail.readonly` instead of `gmail.modify` unless explicitly required).

### 8.3 Accountability
* **Audit Logs:** Immutable JSON logs of every intent, plan, and tool call for user review.
* **Action Transparency:** Real-time streaming of execution steps to the UI, allowing for manual interruption (Kill-switch).

---
