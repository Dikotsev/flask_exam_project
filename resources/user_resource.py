from flask_restful import Resource
from flask import request
from managers.users import UserManager
from schemas.decorator import validate_schema
from schemas.user_schemas import UserRegisterSchema, UserLoginSchema
from db import db



class RegisterUser(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return{"token": token},201



class LoginUser(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return{"token": token, "role": "user"}