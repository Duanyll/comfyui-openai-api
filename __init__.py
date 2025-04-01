from .endpoint import Endpoint
from .generate import Generate

NODE_CLASS_MAPPINGS = {
    "OAIAPIEndpoint": Endpoint,
    "OAIAPIGenerate": Generate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OAIAPIEndpoint": "OpenAI API - Endpoint",
    "OAIAPIGenerate": "OpenAI API - Generate",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
