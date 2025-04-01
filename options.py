import json

from comfy.comfy_types import IO

from .iotypes import OAIAPIIO

class OptionTemperature:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CHAT_COMPLETION_OPTIONS,)
    RETURN_NAMES = ("OPTIONS",)
    FUNCTION = "merge"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "temperature": (IO.FLOAT, {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 2.0,
                    "step": 0.1,
                    "tooltip": "Controls randomness in the generated text. Lower values make the output more deterministic",
                }),
            },
            "optional": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Others options to merge with",
                }),
            },
        }

    def merge(self, temperature, options=None):
        if options is None:
            options = {"temperature": temperature}
        else:
            options["temperature"] = temperature
        return (options,)


class OptionMaxTokens:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CHAT_COMPLETION_OPTIONS,)
    RETURN_NAMES = ("OPTIONS",)
    FUNCTION = "merge"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "max_tokens": (IO.INT, {
                    "default": 512,
                    "min": 1,
                    "tooltip": "An upper bound for the number of tokens that can be generated for a response",
                }),
            },
            "optional": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Others options to merge with",
                }),
            },
        }

    def merge(self, max_tokens, options=None):
        if options is None:
            options = {"max_tokens": max_tokens}
        else:
            options["max_tokens"] = max_tokens
        return (options,)


class OptionTopP:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CHAT_COMPLETION_OPTIONS,)
    RETURN_NAMES = ("OPTIONS",)
    FUNCTION = "merge"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "top_p": (IO.FLOAT, {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 1.0,
                    "tooltip": "An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.",
                })
            },
            "optional": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Others options to merge with",
                }),
            },
        }

    def merge(self, top_p, options=None):
        if options is None:
            options = {"top_p": top_p}
        else:
            options["top_p"] = top_p
        return (options,)


class OptionFrequencyPenalty:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CHAT_COMPLETION_OPTIONS,)
    RETURN_NAMES = ("OPTIONS",)
    FUNCTION = "merge"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frequency_penalty": (IO.FLOAT, {
                    "default": 0,
                    "min": -2.0,
                    "max": 2.0,
                    "tooltip": "Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.",
                }),
            },
            "optional": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Others options to merge with",
                }),
            },
        }

    def merge(self, frequency_penalty, options=None):
        if options is None:
            options = {"frequency_penalty": frequency_penalty}
        else:
            options["frequency_penalty"] = frequency_penalty
        return (options,)


class OptionPresencePenalty:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CHAT_COMPLETION_OPTIONS,)
    RETURN_NAMES = ("OPTIONS",)
    FUNCTION = "merge"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "presence_penalty": (IO.FLOAT, {
                    "default": 0,
                    "min": -2.0,
                    "max": 2.0,
                    "tooltip": "Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.",
                }),
            },
            "optional": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Others options to merge with",
                }),
            },
        }

    def merge(self, presence_penalty, options=None):
        if options is None:
            options = {"presence_penalty": presence_penalty}
        else:
            options["presence_penalty"] = presence_penalty
        return (options,)


class OptionExtraBody:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (OAIAPIIO.CHAT_COMPLETION_OPTIONS,)
    RETURN_NAMES = ("OPTIONS",)
    FUNCTION = "merge"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "extra_body": (IO.STRING, {
                    "default": json.dumps({"repetition_penalty": 0.5, "seed": 42}, indent=4),
                    "tooltip": "Extra body content to include in the request",
                    "multiline": True,
                }),
            },
            "optional": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Others options to merge with",
                }),
            },
        }

    @classmethod
    def VALIDATE_INPUTS(cls, extra_body):
        try:
            data = json.loads(extra_body)
            if not isinstance(data, dict):
                return "must be a JSON object (dictionary)"
        except json.JSONDecodeError as e:
            return f"Invalid JSON: {e}"
        return True

    def merge(self, extra_body, options=None):
        if options is None:
            options = json.loads(extra_body)
        else:
            options = dict(options)
            options.update(json.loads(extra_body))
        return (options,)


class OptionDebug:
    CATEGORY = "OpenAI API"
    RETURN_TYPES = (IO.STRING,)
    RETURN_NAMES = ("ENCODED_JSON",)
    FUNCTION = "marshall"
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "options": (OAIAPIIO.CHAT_COMPLETION_OPTIONS, {
                    "tooltip": "Options chain you want encode",
                }),
            },
        }

    def marshall(self, options):
        return (json.dumps(options, indent=4),)
