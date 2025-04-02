from .client import Client
from .completions import ChatCompletion
from .debug import Debug
from .options import OptionSeed, OptionTemperature, OptionMaxTokens, OptionTopP, OptionFrequencyPenalty, OptionPresencePenalty, OptionExtraBody

NODE_CLASS_MAPPINGS = {
    "OAIAPIClient": Client,
    "OAIAPIChatCompletion": ChatCompletion,
    "OAIAPIDebug": Debug,
    "OAIAPISeed": OptionSeed,
    "OAIAPITemperature": OptionTemperature,
    "OAIAPIMaxTokens": OptionMaxTokens,
    "OAIAPITopP": OptionTopP,
    "OAIAPIFrequencyPenalty": OptionFrequencyPenalty,
    "OAIAPIPresencePenalty": OptionPresencePenalty,
    "OAIAPIExtraBody": OptionExtraBody,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OAIAPIClient": "OpenAI API - Client",
    "OAIAPIChatCompletion": "OpenAI API - Chat Completion",
    "OAIAPIDebug": "OpenAI API - Debug",
    "OAIAPISeed": "OpenAI API - Seed",
    "OAIAPITemperature": "OpenAI API - Temperature",
    "OAIAPIMaxTokens": "OpenAI API - Max Tokens",
    "OAIAPITopP": "OpenAI API - Top P",
    "OAIAPIFrequencyPenalty": "OpenAI API - Frequency Penalty",
    "OAIAPIPresencePenalty": "OpenAI API - Presence Penalty",
    "OAIAPIExtraBody": "OpenAI API - Extra Body",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
