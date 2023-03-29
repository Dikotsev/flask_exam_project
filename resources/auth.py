from flask import request
from werkzeug.security import generate_password_hash
from flask_api import status
from flask_restful import Resource
from passlib.hash import sha256_crypt
from db import db
from schemas.decorator import validate_schema
from schemas.user_schemas import UserLoginSchema, UserSchema
from models.auth import AuthManager
from models.user import BaseUserModel

validate_schema = validate_schema()

class RegisterResource(Resource):
    @validate_schema(UserSchema)
    def post(self):
        data = request.get_json()
        data["password"] = data["password"] = generate_password_hash(data['password'], method='sha256')
        user = BaseUserModel(**data)
        db.session.add(user)
        db.session.commit()
        token = AuthManager.encode_token()
        return {"token": token}, 201


class LoginResource(Resource):
    pass


class LogoutResource(Resource):
    pass