import redis
import json
from typing import Optional, List, Dict
from app.core.config import get_settings

settings = get_settings()

class ShortTermMemory:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            decode_responses=True
        )

    def save_context(self, session_id: str, messages: List[Dict[str, str]]):
        self.client.setex(
            f"session:{session_id}",
            1800,  # 30 minutes TTL
            json.dumps(messages)
        )

    def get_context(self, session_id: str) -> List[Dict[str, str]]:
        data = self.client.get(f"session:{session_id}")
        return json.loads(data) if data else []

    def clear_context(self, session_id: str):
        self.client.delete(f"session:{session_id}")

class LongTermMemory:
    def __init__(self):
        # Placeholder for ChromaDB integration
        pass

    def store_fact(self, user_id: str, fact: str):
        # Implementation for vector embedding and storage
        pass

    def retrieve_relevant(self, query: str, limit: int = 5):
        # Implementation for semantic search
        return []

    def prune_memory(self, threshold: float):
        # Logic for removing low-utility vectors
        pass
