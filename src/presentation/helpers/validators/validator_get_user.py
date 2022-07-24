from cerberus import Validator
from src.presentation.interface import Validator as ValidatorInterface


class ValidatorPayloadHeaderToken(ValidatorInterface):
    def validate(self, data: dict) -> bool:
        schema = {
            "id": {"type": "integer", "required": True},
            "email": {
                "type": "string",
                "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
                "required": True,
            },
        }
        validator = Validator(schema)
        return validator.validate(data)
