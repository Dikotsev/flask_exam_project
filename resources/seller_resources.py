from flask_restful import Resource
from flask import request
from managers.users import SellerManager
from schemas.decorator import validate_schema
from schemas.user_schemas import UserRegisterSchema, UserLoginSchema
from db import db



class RegisterSeller(Resource):
    @validate_schema(UserRegisterSchema)
    def post(self):
        data = request.get_json()
        token = SellerManager.register(data)
        return{"token":token },201



class LoginSeller(Resource):
    @validate_schema(UserLoginSchema)
    def post(self):
        data = request.get_json()
        token = SellerManager.login(data)
        return{"token":token, "role":"seller"}