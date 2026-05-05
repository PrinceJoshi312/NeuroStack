# 6. 🖥️ UI/UX Design Principles

### Core Principles

* **Action Transparency:** Never hide the agent's thought process; show hierarchical steps in real-time.
* **Consent-First Interaction:** High-stakes actions require explicit user confirmation (HITL).
* **Immediate Intervention:** A global "Kill-switch" must be accessible at all times during active execution.
* **Minimal Friction with Maximum Safety:** Use smart defaults for non-critical tasks but escalate visibility for high-impact actions.

---

### UI Components

#### 1. Unified Chat & Action Interface
* **Streaming Responses:** Real-time text generation with embedded action citations.
* **Live Action Log:** A collapsible feed showing the "Agent Brain" steps: `Thought` -> `Plan` -> `Tool Call` -> `Observation`.
* **Global Kill-switch:** A high-visibility button (e.g., Red 'Stop' icon) that terminates the current execution chain and rolls back state where possible.

#### 2. HITL (Human-in-the-Loop) Modal
* **Transaction Summary:** Clearly displays the action, target, and potential impact (e.g., "Delete 5 files?", "Send email to Prince?").
* **Decision Controls:** Explicit `Approve`, `Modify`, or `Reject` buttons.
* **Budget Warning:** Alerts the user if a task is projected to exceed the remaining session token budget.

#### 3. Memory & Privacy Dashboard
* **Semantic Explorer:** Visual representation of stored long-term memory clusters.
* **"Forget" UI:** Contextual buttons next to memory items to trigger deletion (Right to be Forgotten).
* **Permission Manager:** Toggle switch for tool-specific OAuth scopes and API key health status.

#### 4. Multimodal Feedback
* **Visual Status Indicators:** Color-coded status for the agent (e.g., Pulse Blue = Thinking, Solid Green = Ready, Flashing Orange = Waiting for HITL).
* **Voice Transcription Overlay:** Real-time text overlay during voice interaction for verification.

---
