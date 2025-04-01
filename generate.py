from comfy.comfy_types import IO
from server import PromptServer

from .iotypes import OAIAPIIO

class Generate:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (IO.STRING,)
    RETURN_NAMES = ("Response",)
    FUNCTION = "generate"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "endpoint": (OAIAPIIO.CLIENT,),
                "model": (IO.STRING, {
                    "placeholder": "Model name",
                    "tooltip": "The model to use for generating text",
                }),
                "prompt": (IO.STRING, {
                    "placeholder": "User prompt is mandatory",
                    "tooltip": "The prompt to send to the OpenAI API",
                    "multiline": True,
                }),
            },
            "optional": {
                "system_prompt": (IO.STRING, {
                    "placeholder": "Enter a system prompt if needed",
                    "tooltip": "The system prompt to send along with the user prompt",
                    "multiline": True,
                }),
            },
        }

    @classmethod
    def VALIDATE_INPUTS(cls, model, prompt):
        if model == "" or prompt == "":
            return False
        return True

    def generate(self, endpoint, model, prompt, system_prompt=None):
        return ("",)
