"""
Establishes rules in the API
"""
ALLOWED_ATTR_FOR_AUTHOR: list = ["name"]
ALLOWED_ATTR_FOR_POEM: list = ["by-line"]
ALLOWED_ATTR_FOR_POEM_EXACT: list = ["age", "author", "by-line", "title", "type"]
ALLOWED_ATTR_FOR_POEM_LIKE: list = ALLOWED_ATTR_FOR_POEM_EXACT + ["content"]
