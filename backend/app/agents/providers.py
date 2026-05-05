from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class LLMProvider(ABC):
    @abstractmethod
    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        pass

    @abstractmethod
    async def generate_plan(self, prompt: str, **kwargs) -> List[Dict[str, Any]]:
        pass

class GeminiProvider(LLMProvider):
    def __init__(self, api_key: str):
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        # Simplified conversion for demonstration
        chat = self.model.start_chat()
        response = chat.send_message(messages[-1]["content"])
        return response.text

    async def generate_plan(self, prompt: str, **kwargs) -> List[Dict[str, Any]]:
        # In a real implementation, we would use structured output/function calling
        response = self.model.generate_content(prompt)
        return [{"step": "analyze", "content": response.text}]

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key: str):
        from openai import AsyncOpenAI
        self.client = AsyncOpenAI(api_key=api_key)

    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=messages,
            **kwargs
        )
        return response.choices[0].message.content

    async def generate_plan(self, prompt: str, **kwargs) -> List[Dict[str, Any]]:
        # Structured output logic here
        return []

class ClaudeProvider(LLMProvider):
    def __init__(self, api_key: str):
        from anthropic import AsyncAnthropic
        self.client = AsyncAnthropic(api_key=api_key)

    async def generate_response(self, messages: List[Dict[str, str]], **kwargs) -> str:
        response = await self.client.messages.create(
            model="claude-3-opus-20240229",
            messages=messages,
            max_tokens=4096,
            **kwargs
        )
        return response.content[0].text

    async def generate_plan(self, prompt: str, **kwargs) -> List[Dict[str, Any]]:
        return []
