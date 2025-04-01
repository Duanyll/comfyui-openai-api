from .client import Client
from .completions import ChatCompletion

NODE_CLASS_MAPPINGS = {
    "OAIAPIClient": Client,
    "OAIAPIChatCompletion": ChatCompletion,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OAIAPIClient": "OpenAI API - Client",
    "OAIAPIChatCompletion": "OpenAI API - Chat Completion",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
