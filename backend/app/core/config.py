from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "AgentOS"
    gemini_api_key: str
    database_url: str = "sqlite:///./agentos.db"
    redis_host: str = "localhost"
    redis_port: int = 6379
    secret_key: str
    algorithm: str = "HS256"
    max_tokens_per_session: int = 50000
    budget_cap_usd: float = 1.00

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_settings():
    return Settings()
