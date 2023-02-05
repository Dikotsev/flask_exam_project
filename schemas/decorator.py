from functools import wraps
from flask import request


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema = schema_name()
            errors = schema.validate(request.get_json())
            if errors:
                abort (400, errors = errors)
            return f(*args, **kwargs)
        return decorated_function()
    return decorator()