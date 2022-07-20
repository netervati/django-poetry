"""
API mappers
"""


ALLOWED_ATTR_FOR_POEM_EXACT = ["age", "author", "title", "type"]


ALLOWED_ATTR_FOR_POEM_LIKE = ALLOWED_ATTR_FOR_POEM_EXACT + ["content"]


class ListMapper:
    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return {"total_records": len(self.data), "data": self.data}
