from typing import List, Dict, Any
from app.agents.providers import LLMProvider, GeminiProvider, OpenAIProvider, ClaudeProvider
from app.memory.tiered_memory import ShortTermMemory, LongTermMemory
from app.core.config import get_settings
from app.core.safety import BudgetMonitor, KillSwitch

settings = get_settings()

class AgentOrchestrator:
    def __init__(self, provider_name: str = "gemini"):
        self.settings = settings
        self.short_memory = ShortTermMemory()
        self.long_memory = LongTermMemory()
        self.budget_monitor = BudgetMonitor()
        self.kill_switch = KillSwitch()
        self.provider = self._get_provider(provider_name)

    def _get_provider(self, name: str) -> LLMProvider:
        if name == "gemini":
            return GeminiProvider(self.settings.gemini_api_key)
        elif name == "openai":
            # Assuming OPENAI_API_KEY is in settings
            return OpenAIProvider(getattr(self.settings, "openai_api_key", ""))
        elif name == "claude":
            # Assuming CLAUDE_API_KEY is in settings
            return ClaudeProvider(getattr(self.settings, "claude_api_key", ""))
        else:
            raise ValueError(f"Unknown provider: {name}")

    async def handle_user_request(self, session_id: str, user_input: str):
        # 1. Safety Check
        if not self.budget_monitor.is_within_budget(session_id):
            return {"response": "Error: Session budget exceeded.", "actions_taken": [], "plan": []}
        
        if not self.kill_switch.is_active(session_id):
            return {"response": "Error: Execution terminated by kill-switch.", "actions_taken": [], "plan": []}

        # 2. Retrieve Context
        context = self.short_memory.get_context(session_id)
        
        # 3. Add to context
        context.append({"role": "user", "content": user_input})
        
        # 4. Generate Response
        response = await self.provider.generate_response(context)
        
        # 5. Update Budget (Mock token count for now)
        self.budget_monitor.update_usage(session_id, len(user_input) + len(response))
        
        # 6. Save Context
        context.append({"role": "assistant", "content": response})
        self.short_memory.save_context(session_id, context)
        
        return {
            "response": response,
            "actions_taken": [{"type": "thought", "description": "Analyzing user intent and checking safety budget."}],
            "plan": []
        }
