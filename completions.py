import hashlib
import json

from comfy.comfy_types import IO

from .iotypes import OAIAPIIO

class ChatCompletion:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (IO.STRING,)
    RETURN_NAMES = ("Response",)
    FUNCTION = "generate"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "client": (OAIAPIIO.CLIENT,),
                "model": (IO.STRING, {
                    "placeholder": "Model name",
                    "tooltip": "The model to use for generating text",
                }),
                "prompt": (IO.STRING, {
                    "placeholder": "User prompt is mandatory",
                    "tooltip": "The user prompt to send to the OpenAI API",
                    "multiline": True,
                }),
            },
            "optional": {
                "system_prompt": (IO.STRING, {
                    "placeholder": "System/Developer prompt is optional",
                    "tooltip": "The system prompt to send along with the user prompt",
                    "multiline": True,
                }),
                "use_developer_role": (IO.BOOLEAN, {
                    "default": False,
                    "tooltip": "With o1 models and newer, OpenAI has changed the 'system' prompt role to 'developper' prompt role. Set this switch to true to set the system prompt as 'developper'.",
                }),
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "default": None,
                    "tooltip": "Chat completion options. This can be used to specify additional parameters for the chat completion request.",
                })
            },
        }

    @classmethod
    def IS_CHANGED(s, client, model, prompt, system_prompt="", use_developer_role=False, options=None):
        # User might want to regenerate even if we have not changed
        return float("NaN")

    @classmethod
    def VALIDATE_INPUTS(cls, model, prompt):
        if model == "":
            return "model must be specified"
        if prompt == "":
            return "prompt must be specified"
        return True

    def generate(self, client, model, prompt, system_prompt=None, use_developer_role=False, options=None):
        # Create messages
        messages = []
        if system_prompt:
            messages.append({
                "role": "developer" if use_developer_role else "system",
                "content": system_prompt,
            })
        messages.append({"role": "user", "content": prompt})
        # Handle official options
        if options is None:
            options = {}
        if hasattr(options, "temperature"):
            temperature = options["temperature"]
            delattr(options, "temperature")
        else:
            temperature = None
        if hasattr(options, "max_tokens"):
            max_tokens = options["max_tokens"]
            delattr(options, "max_tokens")
        else:
            max_tokens = None
        if hasattr(options, "top_p"):
            top_p = options["top_p"]
            delattr(options, "top_p")
        else:
            top_p = None
        if hasattr(options, "frequency_penalty"):
            frequency_penalty = options["frequency_penalty"]
            delattr(options, "frequency_penalty")
        else:
            frequency_penalty = None
        if hasattr(options, "presence_penalty"):
            presence_penalty = options["presence_penalty"]
            delattr(options, "presence_penalty")
        else:
            presence_penalty = None
        # Create the completion
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            extra_body=options

        )
        return (completion.choices[0].message.content,)
