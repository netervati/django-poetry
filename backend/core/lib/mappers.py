"""
API mappers
"""
from typing import Union


ALLOWED_ATTR_FOR_AUTHOR: list = ["name"]
ALLOWED_ATTR_FOR_POEM: list = ["by-line"]
ALLOWED_ATTR_FOR_POEM_EXACT: list = ["age", "author", "by-line", "title", "type"]
ALLOWED_ATTR_FOR_POEM_LIKE: list = ALLOWED_ATTR_FOR_POEM_EXACT + ["content"]


class RecordMapper:
    def __init__(self, data: Union[list, dict]):
        self.data = data

    def to_dict(self) -> dict:
        return {"attributes": self.data}


class ListMapper(RecordMapper):
    def to_dict(self) -> dict:
        return {"total_records": len(self.data), "attributes": self.data}
