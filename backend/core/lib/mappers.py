"""
API mappers
"""


ALLOWED_ATTR_FOR_AUTHOR = ["name"]
ALLOWED_ATTR_FOR_POEM = ["by-line"]
ALLOWED_ATTR_FOR_POEM_EXACT = ["age", "author", "title", "type"]
ALLOWED_ATTR_FOR_POEM_LIKE = ALLOWED_ATTR_FOR_POEM_EXACT + ["content"]


class RecordMapper:
    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {"data": self.data}


class ListMapper(RecordMapper):
    def to_dict(self):
        return {"total_records": len(self.data), "data": self.data}
