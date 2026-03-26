**NeuroStack**

**Offline AI Virtual Assistant**

Project Documentation Suite --- v1.0 \| 2026

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------
  **Version**                1.0 --- Initial Release
  -------------------------- --------------------------------------------
  **Status**                 Pre-Development

  **Year**                   2026

  **Architecture**           Local-First, Agent-Based AI
  -----------------------------------------------------------------------

> **1. Project Assessment & Critical Review**

**1.1 What Makes NeuroStack a Strong Idea**

NeuroStack addresses a genuine and growing need: a private,
offline-capable AI assistant with agent-level reasoning. The original
concept has several notable strengths:

-   Offline-first design avoids API costs and privacy risks inherent in
    cloud-based LLMs.

-   Modular MCP-based tool architecture is aligned with the direction
    the broader AI industry is moving (Anthropic, LangChain, and others
    have adopted MCP as a standard).

-   Phased development roadmap is realistic for a solo or small-team
    project.

-   Technology choices (Ollama, LangGraph, ChromaDB) are
    well-established, actively maintained, and have good community
    support.

-   The vision of combining RAG + Agents + Voice + Automation in one
    stack is technically coherent.

**1.2 Issues Found & Corrections Made**

The following issues were identified in the original SRS and have been
corrected in this documentation:

  -------------------------------------------------------------------------------
  **\#**   **Original       **Problem**             **Correction Applied**
           Issue**                                  
  -------- ---------------- ----------------------- -----------------------------
  1        Agent Framework  AutoGen v0.2 is         Replaced with LangGraph as
           listed AutoGen   deprecated. AutoGen     primary (stable,
                            v0.4 has breaking       production-ready). AutoGen
                            changes and a           v0.4 noted as optional
                            completely different    advanced choice only.
                            API.                    

  2        Phi-3 listed as  Phi-3 has been          Updated to Phi-4 14B. Still
           lightweight LLM  superseded by Phi-4     lightweight vs Llama 70B;
                            (2025), which has       better for CPU-only setups
                            superior performance on with 16 GB RAM.
                            reasoning and coding    
                            tasks.                  

  3        Coqui TTS listed Coqui TTS               Replaced with Kokoro-TTS
           in voice stack   (coqui-ai/TTS) was      (2025, near-human quality) as
                            archived and is no      primary, Piper TTS as
                            longer actively         reliable fallback.
                            maintained as of late   
                            2024.                   

  4        Hardware         Running a 70B model on  Hardware requirements now
           minimums not     16 GB RAM is not        broken down by model tier
           differentiated   feasible. The original  with specific RAM/VRAM
           by model         guidance was misleading mappings per model size.
                            for beginners.          

  5        No mention of    Without quantization    GGUF / Q4_K_M quantization
           quantization     guidance, users may try added throughout. This is
                            to run full-precision   essential for local
                            models that exceed      deployment on consumer
                            their hardware.         hardware.

  6        No testing or    An AI assistant without Testing strategy section
           evaluation       evaluation criteria has added: unit tests,
           strategy         no way to measure       integration tests, and LLM
                            progress, quality, or   response evaluation with
                            regression.             golden prompts.

  7        Week 6 UI phase  UI approach was         Specified as Gradio (fastest
           had no           entirely unspecified    to build) or Tauri-based
           specification    --- web UI? desktop     desktop app (best production
                            app? TUI? --- leading   UX).
                            to scope ambiguity.     
  -------------------------------------------------------------------------------

> **2. System Requirements Specification (SRS)**

**2.1 Vision & Purpose**

+-----------------------------------------------------------------------+
| **NeuroStack is an offline-first, modular AI virtual assistant        |
| running entirely on local hardware.**                                 |
|                                                                       |
| It combines a local LLM, vector memory, MCP-based tool use, voice     |
| I/O, and agentic planning                                             |
|                                                                       |
| into a unified, privacy-preserving personal AI platform --- with zero |
| recurring API cost.                                                   |
+=======================================================================+
+-----------------------------------------------------------------------+

**2.2 Functional Requirements**

**FR-1: Conversation Engine**

-   Multi-turn chat with a local LLM (Ollama backend)

-   Configurable system personality / persona via YAML

-   Short-term context window memory (last N turns)

-   Graceful handling of context overflow via summarization

**FR-2: Memory System**

-   Short-term: in-context conversation history

-   Long-term: vector DB (ChromaDB) for semantic recall

-   User preference storage (JSON or SQLite)

-   Episodic memory: store and retrieve past interactions by topic

**FR-3: Tool Use via MCP**

-   File system read / write / search

-   Code execution in a sandboxed environment

-   OS automation (open apps, control system settings)

-   Optional web search via local SearxNG instance

-   Calendar and reminder management

**FR-4: Voice Interface**

-   Offline speech-to-text via faster-whisper

-   Offline text-to-speech via Piper TTS (stable) or Kokoro-TTS (high
    quality)

-   Optional wake word detection via OpenWakeWord

-   Push-to-talk mode as a lightweight alternative to wake word

**FR-5: Agentic Behavior**

-   Task decomposition --- break user goals into sub-steps

-   Multi-step planning with LangGraph state machine

-   Tool chaining --- pass output from one tool as input to another

-   Self-reflection loop --- re-evaluate plan if tool calls fail

**FR-6: Multimodal (Phase 2+)**

-   Image understanding via local vision model (LLaVA or Qwen-VL)

-   Document Q&A via PDF / DOCX ingestion to vector DB

-   Screenshot analysis for screen-aware assistance

**2.3 Non-Functional Requirements**

  --------------------------------------------------------------------------
  **Requirement**     **Specification**
  ------------------- ------------------------------------------------------
  **Privacy**         All processing must occur locally. No data sent to
                      external APIs by default.

  **Latency**         Text response \< 3 s on recommended hardware. Voice
                      pipeline round-trip \< 5 s.

  **Modularity**      Each component (LLM, memory, tools, voice) must be
                      independently replaceable.

  **Offline-First**   Core functionality must work with no internet
                      connection. Network features are optional add-ons.

  **Config-Driven**   All major parameters (model, memory size, tool list,
                      persona) controlled via a single YAML config.

  **Portability**     Must run on Windows 11, Ubuntu 22+, and macOS 13+.
                      Docker support for environment consistency.
  --------------------------------------------------------------------------

> **3. Corrected & Final Technology Stack**

**3.1 Local LLM Selection**

All models should be run in GGUF format with Q4_K_M quantization for the
best balance of quality and RAM usage. Use Ollama as the inference
server.

  ------------------------------------------------------------------------
  **Model**      **Size     **Min     **Best Use Case**
                 (Q4)**     RAM**     
  -------------- ---------- --------- ------------------------------------
  Llama 3.1 8B   \~5 GB     8 GB      Recommended start. Good general
                                      chat, fast on CPU.

  Llama 3.1 70B  \~40 GB    48+ GB    Highest quality. Requires high-end
                                      hardware (GPU strongly recommended).

  Mistral 7B     \~4.5 GB   8 GB      Fast reasoning, strong coding
                                      ability. Good Llama 3.1 8B
                                      alternative.

  Phi-4 14B      \~8 GB     16 GB     Excellent reasoning per parameter.
                                      Best for CPU-only setups with 16 GB
                                      RAM.

  Qwen2.5 7B     \~5 GB     8 GB      Strong multilingual + code. Good alt
                                      if Llama licensing is a concern.
  ------------------------------------------------------------------------

**3.2 Complete Corrected Stack**

  ------------------------------------------------------------------------
  **Component**    **Technology         **Why This Choice**
                   (Corrected)**        
  ---------------- -------------------- ----------------------------------
  LLM Runtime      Ollama               Easiest local setup. Manages
                                        models, GGUF, GPU offload
                                        automatically.

  Primary LLM      Llama 3.1 8B         Best balance of quality and RAM
                   (Q4_K_M)             for most hardware. Start here.

  Agent Framework  LangGraph            Graph-based agent state machine.
                                        Production-ready, actively
                                        maintained.

  Vector Memory    ChromaDB             Embedded, no server needed,
                                        Python-native. Great for local
                                        deployment.

  Embeddings       all-MiniLM-L6-v2     Fast, small, offline. \~90 MB
                                        download. Excellent for semantic
                                        search.

  Tool Protocol    MCP Python SDK       Anthropic-standard tool protocol.
                                        Growing ecosystem of ready-made
                                        tools.

  Speech-to-Text   faster-whisper       CTranslate2-optimized. 4x faster
                   (Whisper v3)         than original Whisper. Fully
                                        offline.

  Text-to-Speech   Kokoro-TTS (primary) Kokoro (2025) produces near-human
                   / Piper TTS          quality offline. Piper is
                   (fallback)           battle-tested.

  Wake Word        OpenWakeWord         Free, offline, customizable.
                                        Alternative: Porcupine (freemium,
                                        higher accuracy).

  UI (Phase 5)     Gradio (quick) or    Gradio in \< 20 lines of Python.
                   Tauri (desktop app)  Tauri for a native desktop
                                        experience.

  Config Format    YAML + Pydantic      Single config.yaml drives all
                   validation           parameters. Pydantic ensures
                                        schema safety.
  ------------------------------------------------------------------------

> **4. System Architecture**

**4.1 Architecture Overview**

NeuroStack follows a four-layer architecture: Interface, Orchestration,
Services, and Storage.

+-----------------------------------------------------------------------+
| **INTERFACE LAYER Voice (STT / TTS / Wake Word) \| Text UI \| REST    |
| API**                                                                 |
|                                                                       |
| ORCHESTRATION LAYER Core Agent (LangGraph) \| Planner \| MCP Tool     |
| Router                                                                |
|                                                                       |
| SERVICES LAYER LLM (Ollama) \| Memory \| Tools \| Voice Pipeline      |
|                                                                       |
| STORAGE LAYER ChromaDB \| SQLite \| File System \| Model Cache        |
+=======================================================================+
+-----------------------------------------------------------------------+

**4.2 Data Flow --- Standard Request**

  -----------------------------------------------------------------------------
  **Step**   **Component**      **Action**
  ---------- ------------------ -----------------------------------------------
  1          Voice / UI Input   User speaks or types a query. Voice is
                                transcribed offline by faster-whisper.

  2          Core Agent         LangGraph agent receives the query and decides:
                                direct answer vs. tool call vs. multi-step
                                plan.

  3          Memory Retrieval   ChromaDB is queried for relevant past context
                                using semantic similarity search.

  4          LLM (Ollama)       Query + retrieved memory + tool outputs are
                                assembled into a prompt. Ollama returns a
                                response.

  5          MCP Tool Router    If the LLM requests a tool call, the router
                                dispatches to the appropriate MCP server.

  6          Tool Execution     File system, code runner, OS control, or web
                                search tool executes and returns a result.

  7          Response Assembly  Agent assembles final response. Memory system
                                stores the exchange in ChromaDB.

  8          Output             Response is spoken via Kokoro/Piper TTS (voice
                                mode) or displayed in the UI (text mode).
  -----------------------------------------------------------------------------

**4.3 Project Folder Structure**

+-----------------------------------------------------------------------+
| **NeuroStack/**                                                       |
|                                                                       |
| core/ agent.py \| planner.py \| router.py \| config.py                |
|                                                                       |
| llm/ ollama_client.py \| prompt_builder.py                            |
|                                                                       |
| memory/ short_term.py \| vector_db.py \| user_prefs.py                |
|                                                                       |
| tools/ file_tool.py \| code_tool.py \| system_tool.py \| web_tool.py  |
|                                                                       |
| voice/ stt.py \| tts.py \| wake_word.py                               |
|                                                                       |
| mcp/ servers/ \| tool_registry.py                                     |
|                                                                       |
| ui/ gradio_app.py \| (tauri_app/ --- Phase 5)                         |
|                                                                       |
| tests/ unit/ \| integration/ \| evals/                                |
|                                                                       |
| config.yaml --- single source of truth for all parameters             |
|                                                                       |
| main.py --- entry point                                               |
|                                                                       |
| requirements.txt                                                      |
+=======================================================================+
+-----------------------------------------------------------------------+

> **5. Development Roadmap (6 Phases)**

  -----------------------------------------------------------------------------
  **Phase**   **Timeline**   **Goals**                    **Deliverable**
  ----------- -------------- ---------------------------- ---------------------
  Phase 1     Week 1--2      Install Ollama. Run Llama    Working CLI chatbot
                             3.1 8B. Build CLI chat loop. with local LLM.
                             Add basic config.yaml.       
                             Implement short-term memory. 

  Phase 2     Week 3--4      Integrate LangGraph agent.   Agentic assistant
                             Add MCP tool protocol.       that can execute
                             Implement file, code, and OS tasks.
                             control tools. Test tool     
                             chaining.                    

  Phase 3     Week 5--6      Integrate ChromaDB for       Personalized
                             long-term memory. Implement  assistant with
                             sentence-transformer         semantic recall.
                             embeddings. Build user       
                             preference storage.          

  Phase 4     Week 7--8      Add faster-whisper STT. Add  Full voice
                             Kokoro or Piper TTS.         interaction
                             Implement push-to-talk.      capability.
                             Optionally add OpenWakeWord. 

  Phase 5     Week 9--10     Build Gradio or Tauri UI.    Desktop or web UI for
                             Add conversation history     the assistant.
                             display. Implement settings  
                             panel. Polish overall UX.    

  Phase 6     Week 11--12    Multi-agent setup (planner + Autonomous
                             executor + memory agents).   multi-agent
                             Add LLaVA for image          NeuroStack.
                             understanding. Performance   
                             tuning.                      
  -----------------------------------------------------------------------------

> **6. Hardware Requirements (Corrected)**

Hardware requirements depend heavily on the model you choose to run. The
table below maps tiers clearly.

  -------------------------------------------------------------------------------
  **Tier**          **RAM / VRAM**   **Recommended      **Experience**
                                     Model**            
  ----------------- ---------------- ------------------ -------------------------
  **Minimum**       8 GB RAM, CPU    Llama 3.1 8B Q4 or Usable. Responses may
                    only             Phi-4 14B Q4       take 10--30 s. Good for
                                                        development.

  **Recommended**   16 GB RAM or 8   Llama 3.1 8B or    Smooth experience, fast
                    GB VRAM GPU      Mistral 7B         responses (2--5 s). Good
                                                        for daily use.

  **Performance**   32 GB RAM + RTX  Llama 3.1 70B Q4   Near real-time responses
                    3060 12 GB       (partial GPU)      with full reasoning
                                                        capability.

  **Ultra**         64 GB RAM + RTX  Llama 3.1 70B or   Production-grade.
                    4090 24 GB       Mixtral 8x22B      Multiple simultaneous
                                                        model instances possible.
  -------------------------------------------------------------------------------

+-----------------------------------------------------------------------+
| **Note on Quantization:**                                             |
|                                                                       |
| Always use Q4_K_M GGUF format via Ollama for the best quality-to-RAM  |
| ratio.                                                                |
|                                                                       |
| Q4_K_M reduces a 70B model from \~140 GB (FP16) to \~40 GB with       |
| minimal quality loss.                                                 |
|                                                                       |
| Command: ollama pull llama3.1:8b-instruct-q4_K_M                      |
+=======================================================================+
+-----------------------------------------------------------------------+

> **7. Testing Strategy**

A structured testing approach prevents quality regression as NeuroStack
grows. Three levels of testing are required.

**7.1 Unit Tests**

-   Test each tool in isolation (file_tool, code_tool, system_tool) with
    mocked outputs.

-   Test the prompt builder to ensure context is assembled correctly
    from memory + history.

-   Test ChromaDB insert and retrieve with known embeddings and expected
    similarity scores.

-   Test config.yaml validation via Pydantic schema to catch bad
    configuration early.

**7.2 Integration Tests**

-   Test full agent loop: user input → LLM → tool call → response, end
    to end.

-   Test voice pipeline end-to-end with a pre-recorded WAV file.

-   Test memory persistence across simulated conversation sessions.

-   Test MCP server connectivity and tool routing with all registered
    tools.

**7.3 LLM Response Evaluation**

-   Maintain a YAML file of 20--30 golden test prompts with expected
    behavior criteria.

-   Score responses on: relevance, tool usage accuracy, hallucination
    rate, and latency.

-   Run the eval suite after each model upgrade or major prompt change.

-   Recommended tool: deepeval or a custom scoring script for automated
    evaluation.

> **8. Risk Register**

  ------------------------------------------------------------------------------------
  **Risk**              **Probability**   **Impact**   **Mitigation**
  --------------------- ----------------- ------------ -------------------------------
  Hardware bottleneck   High              High         Use Q4_K_M quantization. Start
  --- model too slow on                                with 7--8B models. Add GPU
  available CPU                                        later when budget allows.

  Context window        Medium            Medium       Implement sliding window +
  overflow on long                                     ChromaDB summarization fallback
  conversations                                        for older context.

  MCP tool security --- Low               High         Run code tool inside Docker or
  code execution                                       subprocess with strict resource
  sandbox escape                                       limits (CPU, memory, no
                                                       network).

  LLM hallucination in  Medium            High         Add self-reflection step after
  agentic tasks                                        each tool call. Use confidence
                                                       scoring. Log all tool calls.

  TTS / STT quality on  Medium            Medium       Use Whisper large-v3 for STT.
  non-English or                                       Test with diverse audio samples
  accented speech                                      early in development.

  Dependency rot ---    Low               Medium       Pin all dependencies in
  libraries break on                                   requirements.txt. Use a virtual
  Python version                                       environment. Run tests on
  upgrade                                              upgrade.
  ------------------------------------------------------------------------------------

> **9. Pre-Development Quick-Start Checklist**

Complete all items below before writing any application code:

**Environment Setup**

-   Install Python 3.11+ and create a virtual environment: python -m
    venv .venv

-   Install Ollama from https://ollama.com

-   Pull your chosen model: ollama pull llama3.1:8b-instruct-q4_K_M

-   Verify Ollama is serving: curl http://localhost:11434/api/tags

**Dependencies to Install (pip)**

-   langchain-community, langgraph, langchain-ollama

-   chromadb, sentence-transformers

-   faster-whisper, kokoro-tts (or piper-tts)

-   mcp (Anthropic MCP Python SDK)

-   pydantic, pyyaml, python-dotenv

-   gradio (for Phase 5 UI)

**Repo Initialization**

-   Create the folder structure as defined in Section 4.3

-   Initialize Git: git init && git add . && git commit -m \'initial
    scaffold\'

-   Create config.yaml with model name, memory settings, and tool list

-   Write a smoke test: send \'Hello\' to Ollama via Python, print the
    response

+-----------------------------------------------------------------------+
| **First Milestone (End of Week 1):**                                  |
|                                                                       |
| You type a message in the CLI, the local LLM responds, and the        |
| conversation                                                          |
|                                                                       |
| is saved to a ChromaDB collection. No voice, no tools --- just the    |
| brain.                                                                |
|                                                                       |
| Everything else is built on top of this working foundation.           |
+=======================================================================+
+-----------------------------------------------------------------------+

> **10. Final Stack Summary**

  -----------------------------------------------------------------------
  **Component**    **Technology**         **Why This Choice**
  ---------------- ---------------------- -------------------------------
  LLM Runtime      Ollama                 Easiest local setup.
                                          Auto-manages quantization and
                                          GPU offload.

  Primary Model    Llama 3.1 8B Q4_K_M    Best balance of quality and RAM
                                          for most hardware.

  Agent Framework  LangGraph              Graph-based agent state.
                                          Production-ready, not
                                          deprecated.

  Vector Memory    ChromaDB               Embedded, no server needed,
                                          Python-native.

  Embeddings       all-MiniLM-L6-v2       Fast, small, offline. Excellent
                                          for semantic search.

  Tool Protocol    MCP Python SDK         Industry standard. Growing
                                          ecosystem of tools.

  Speech-to-Text   faster-whisper         4x faster than original
                                          Whisper. Fully offline.

  Text-to-Speech   Kokoro-TTS / Piper TTS Kokoro for quality; Piper for
                                          reliability.

  Wake Word        OpenWakeWord           Free, offline, and
                                          customizable.

  UI               Gradio (prototype) →   Gradio for speed; Tauri for
                   Tauri (prod)           polished desktop UX.

  Config           YAML + Pydantic        Single file drives everything.
                                          Schema validation prevents
                                          bugs.
  -----------------------------------------------------------------------

**NeuroStack --- Offline Intelligence. No clouds. No limits.**

Documentation v1.0 \| Built for local-first AI development \| 2026
