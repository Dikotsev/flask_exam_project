from functools import wraps
from flask import request
from werkzeug.exceptions import BadRequest, Forbidden
from models.auth import auth


def validate_schema(schema_name):
    def decorated_function(f):
        def wrapper(*args,**kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if not errors:
                return f(*args, **kwargs)
            raise BadRequest (f"Invalid fields{errors}")
        return wrapper
    return decorated_function



def permission_required(role):
    def decorated_function(f):
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()
            if not current_user.role == role:
                raise Forbidden("Permission denied!")
            return f(*args, **kwargs)
        return wrapper
    return decorated_function


