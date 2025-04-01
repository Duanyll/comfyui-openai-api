import json

from comfy.comfy_types import IO

from .iotypes import OAIAPIIO

class ChatCompletion:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (IO.STRING, IO.STRING)
    RETURN_NAMES = ("Response", "Debug")
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
            },
        }

    @classmethod
    def VALIDATE_INPUTS(cls, model, prompt):
        if model == "" or prompt == "":
            return False
        return True

    def generate(self, client, model, prompt, system_prompt=None, use_developer_role=False):
        messages = []
        if system_prompt:
            messages.append({
                "role": "developer" if use_developer_role else "system",
                "content": system_prompt,
            })
        messages.append({"role": "user", "content": prompt})
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        print(messages)
        return (completion.choices[0].message.content,)
