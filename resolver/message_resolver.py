import json

from utility.custom_logger import root_logger


class MessageResolver:
    def __init__(self):
        pass

    @staticmethod
    def resolve(message: str):
        root_logger.debug(message)
        request = json.loads(message)
        game_id = request.get("game_id")
        object_id = request.get("object_id")
        operation_id = request.get("operation_id")
        args = request.get("args")
