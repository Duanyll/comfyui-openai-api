from .client import Client
from .completions import ChatCompletion
from .options import OptionTemperature, OptionMaxTokens, OptionTopP, OptionFrequencyPenalty, OptionPresencePenalty, OptionExtraBody, OptionDebug

NODE_CLASS_MAPPINGS = {
    "OAIAPIClient": Client,
    "OAIAPIChatCompletion": ChatCompletion,
    "OAIAPIOptionTemperature": OptionTemperature,
    "OAIAPIOptionMaxTokens": OptionMaxTokens,
    "OAIAPIOptionTopP": OptionTopP,
    "OAIAPIOptionFrequencyPenalty": OptionFrequencyPenalty,
    "OAIAPIOptionPresencePenalty": OptionPresencePenalty,
    "OAIAPIOptionExtraBody": OptionExtraBody,
    "OAIAPIOptionDebug": OptionDebug,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OAIAPIClient": "OpenAI API - Client",
    "OAIAPIChatCompletion": "OpenAI API - Chat Completion",
    "OAIAPIOptionTemperature": "OpenAI API - Option - Temperature",
    "OAIAPIOptionMaxTokens": "OpenAI API - Option - Max Tokens",
    "OAIAPIOptionTopP": "OpenAI API - Option - Top P",
    "OAIAPIOptionFrequencyPenalty": "OpenAI API - Option - Frequency Penalty",
    "OAIAPIOptionPresencePenalty": "OpenAI API - Option - Presence Penalty",
    "OAIAPIOptionExtraBody": "OpenAI API - Option - Extra Body",
    "OAIAPIOptionDebug": "OpenAI API - Option - Debug",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
