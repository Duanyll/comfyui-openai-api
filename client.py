from urllib.parse import urlparse

from comfy.comfy_types import IO
from openai import OpenAI

from .iotypes import OAIAPIIO

class Client:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CLIENT,)
    # RETURN_NAMES = ("Target",)
    FUNCTION = "create_client"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "base_url": (IO.STRING, {
                    "default": "https://api.openai.com/v1",
                    "placeholder": "http(s)://host[:port][/URI]",
                    "tooltip": "The base URL to use for the OpenAI API requests",
                }),
                "max_retries": (IO.INT, {
                    "min": 0,
                    "default": 2,
                    "tooltip": "Maximum number of retries on failure"
                }),
                "timeout": (IO.INT, {
                    "min": 1,
                    "default": 600,
                    "tooltip": "Request timeout in seconds"
                }),
            },
            "optional": {
                "api_key": (IO.STRING, {
                    "tooltip": "The API key to use, if any"
                })
            }
        }

    @classmethod
    def VALIDATE_INPUTS(cls, base_url):
        try:
            result = urlparse(base_url)
            if result.scheme not in ["http", "https"]:
                return "URL scheme must be http or https"
        except ValueError as e:
            return f"invalid URL: {e}"
        return True

    def create_client(self, base_url, api_key=None, max_retries=2, timeout=600):
        return (OpenAI(
            api_key=api_key,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout
        ),)
