from app.core.config import get_settings

settings = get_settings()

class BudgetMonitor:
    def __init__(self):
        self.session_budgets = {} # In-memory for now, could move to Redis

    def update_usage(self, session_id: str, tokens: int):
        if session_id not in self.session_budgets:
            self.session_budgets[session_id] = 0
        self.session_budgets[session_id] += tokens

    def is_within_budget(self, session_id: str) -> bool:
        usage = self.session_budgets.get(session_id, 0)
        return usage < settings.max_tokens_per_session

class KillSwitch:
    def __init__(self):
        self.active_tasks = {}

    def stop_task(self, session_id: str):
        self.active_tasks[session_id] = False

    def is_active(self, session_id: str) -> bool:
        return self.active_tasks.get(session_id, True)

    def start_task(self, session_id: str):
        self.active_tasks[session_id] = True
