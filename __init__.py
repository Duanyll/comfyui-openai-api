from .client import Client
from .completions import ChatCompletion
from .options import OptionTemperature, OptionMaxTokens, OptionTopP, OptionFrequencyPenalty, OptionPresencePenalty, OptionExtraBody, OptionsDebug

NODE_CLASS_MAPPINGS = {
    "OAIAPIClient": Client,
    "OAIAPIChatCompletion": ChatCompletion,
    "OAIAPITemperature": OptionTemperature,
    "OAIAPIMaxTokens": OptionMaxTokens,
    "OAIAPITopP": OptionTopP,
    "OAIAPIFrequencyPenalty": OptionFrequencyPenalty,
    "OAIAPIPresencePenalty": OptionPresencePenalty,
    "OAIAPIExtraBody": OptionExtraBody,
    "OAIAPIDebug": OptionsDebug,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OAIAPIClient": "OpenAI API - Client",
    "OAIAPIChatCompletion": "OpenAI API - Chat Completion",
    "OAIAPITemperature": "OpenAI API - Temperature",
    "OAIAPIMaxTokens": "OpenAI API - Max Tokens",
    "OAIAPITopP": "OpenAI API - Top P",
    "OAIAPIFrequencyPenalty": "OpenAI API - Frequency Penalty",
    "OAIAPIPresencePenalty": "OpenAI API - Presence Penalty",
    "OAIAPIExtraBody": "OpenAI API - Extra Body",
    "OAIAPIDebug": "OpenAI API - Debug",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
