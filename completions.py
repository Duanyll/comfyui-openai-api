import base64
import io

import numpy as np
from PIL import Image

from comfy.comfy_types import IO

from .iotypes import OAIAPIIO

class ChatCompletion:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (IO.STRING, OAIAPIIO.HISTORY)
    RETURN_NAMES = ("RESPONSE", "HISTORY")
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
                "history": (OAIAPIIO.HISTORY, {
                    "default": None,
                    "tooltip": "Chat completions history to send to the OpenAI API. If system prompt is (re)specified it will be overwritten by the new one. If system prompt is not specified, the previous one (if any) will be used.",
                }),
                "options": (OAIAPIIO.OPTIONS, {
                    "default": None,
                    "tooltip": "Chat completion options. This can be used to specify additional parameters for the chat completion request.",
                }),
                "image": (IO.IMAGE, {
                    "default": None,
                    "tooltip": "One or multiples images to send along with the prompt. The model must have multi modals capabilities to process images.",
                })
            },
        }

    @classmethod
    def IS_CHANGED(s, client, model, prompt, system_prompt="", history=None, options=None, image=None):
        # User might want to regenerate even if we have not changed
        return float("NaN")

    @classmethod
    def VALIDATE_INPUTS(cls, model, prompt):
        if model == "":
            return "model must be specified"
        if prompt == "":
            return "prompt must be specified"
        return True

    def generate(self, client, model, prompt, system_prompt=None, history=None, options=None, image=None):
        # Handle options
        seed = None
        temperature = None
        max_tokens = None
        top_p = None
        frequency_penalty = None
        presence_penalty = None
        use_developer_role = False
        if options is not None:
            if "seed" in options:
                seed = options["seed"]
                del options["seed"]
            if "temperature" in options:
                temperature = options["temperature"]
                del options["temperature"]
            if "max_tokens" in options:
                max_tokens = options["max_tokens"]
                del options["max_tokens"]
            if "top_p" in options:
                top_p = options["top_p"]
                del options["top_p"]
            if "frequency_penalty" in options:
                frequency_penalty = options["frequency_penalty"]
                del options["frequency_penalty"]
            if "presence_penalty" in options:
                presence_penalty = options["presence_penalty"]
                del options["presence_penalty"]
            if "use_developer_role" in options:
                use_developer_role = options["use_developer_role"]
                del options["use_developer_role"]
        # Handle system prompt
        system_role = "developer" if use_developer_role else "system"
        if history is not None:
            messages = history.copy()
            if system_prompt is not None:
                # Should we insert it at the beginning or replace the existing system message?
                if history[0]["role"] == "system" or history[0]["role"] == "developer":
                    messages[0]["role"] = system_role
                    messages[0]["content"] = system_prompt
                else:
                    messages.insert(0, {
                        "role": system_role,
                        "content": system_prompt,
                    })
        else:
            messages = []
            if system_prompt:
                messages.append({
                    "role": "developer" if use_developer_role else "system",
                    "content": system_prompt,
                })
        # Handle user message
        if image is not None:
            # Build multi modal content
            content = []
            for batch_image in image:
                content.append(
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_to_base64_png(batch_image)}"
                        }
                    }
                )
            content.append(
                {
                    "type": "text",
                    "text": prompt
                }
            )
            # Add the multi-modal content to the messages list
            messages.append(
                {
                    "role": "user",
                    "content": content,
                }
            )
        else:
            messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )
        # Create the completion
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            seed=seed,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            extra_body=options,
            n=1
        )
        # Return the response and the history
        messages.append(
            {
                "role": completion.choices[0].message.role,
                "content": completion.choices[0].message.content
            }
        )
        return (
            completion.choices[0].message.content,
            messages,
        )


def image_to_base64_png(image):
    # Taken from the SaveImage ComfyUI node
    i = 255. * image.cpu().numpy()
    img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
    # But we do not want it on disk, but in memory as b64
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode('utf-8')
