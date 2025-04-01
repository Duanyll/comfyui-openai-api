from comfy.comfy_types.node_typing import StrEnum

class OAIAPIIO(StrEnum):
    """
    Node input/output data types.
    """
    CLIENT = "CLIENT"
    CHAT_COMPLETION_OPTIONS = "CHAT_COMPLETION_OPTIONS"

