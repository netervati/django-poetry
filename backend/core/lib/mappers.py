"""
Mapper for allowed query parameters in services
"""


ALLOWED_ATTR_FOR_POEM_EXACT = ["age", "author", "title", "type"]


ALLOWED_ATTR_FOR_POEM_LIKE = ALLOWED_ATTR_FOR_POEM_EXACT + ["content"]
