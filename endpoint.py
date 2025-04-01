from urllib.parse import urlparse

from comfy.comfy_types import IO
from server import PromptServer

from .iotypes import OAIAPIIO

class Endpoint:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.ENDPOINT,)
    # RETURN_NAMES = ("Target",)
    FUNCTION = "noop"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "base_url": (IO.STRING, {
                    "default": "https://api.openai.com/v1",
                    "placeholder": "http(s)://host[:port][/URI]",
                    "tooltip": "The base URL to use for the OpenAI API requests",
                })
            },
            "optional": {
                "api_key": (IO.STRING, {
                    "tooltip": "The API key to use, if any"
                })
                # "timeout": (IO.FLOAT, {"default": 30.0, "tooltip": "Request timeout in seconds."}),
                # "max_retries": (IO.INT, {"default": 3, "tooltip": "Maximum number of retries on failure."})
            }
        }
    
    @classmethod
    def VALIDATE_INPUTS(cls, base_url):
        try:
            result = urlparse(base_url)
            if result.scheme not in ["http", "https"]:
                return False
        except ValueError:
            return False
        return True

    def noop(self, base_url, api_key=None):
        # Here you would typically initialize your endpoint object with the provided parameters
        # For now, we'll just return the base_url as a placeholder
        PromptServer.instance.send_sync("example.imageselector.textmessage", {"message":"test"})
        return (EndpointConfig(base_url, api_key),)


class EndpointConfig:
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.api_key = api_key
