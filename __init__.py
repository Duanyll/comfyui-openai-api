from .client import Client
from .generate import Generate

NODE_CLASS_MAPPINGS = {
    "OAIAPIClient": Client,
    "OAIAPIGenerate": Generate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OAIAPIClient": "OpenAI API - Client",
    "OAIAPIGenerate": "OpenAI API - Generate",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
