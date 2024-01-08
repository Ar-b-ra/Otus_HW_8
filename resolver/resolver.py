import json

from utility.custom_logger import root_logger


class Resolver:
    def __init__(self):
        pass

    def resolve(self, message: bytes | str):
        root_logger.debug(message)
        request = json.loads(message)
        game_id = request.get("game_id")
        object_id = request.get("object_id")
        operation_id = request.get("operation_id")
        args = request.get("args")
