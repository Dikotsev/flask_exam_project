from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth import AuthManager
from models.seller import SellerModel
from models.user import UserModel
from models.enum import UserRolesEnum
from db import db




class SellerManager:


    @staticmethod
    def register(seller_data):
        seller = SellerModel(**seller_data)
        try:
            db.session.add(seller)
            db.session.commit()
            return AuthManager.encode_token(seller)
        except Exception as ex:
            raise BadRequest(str(ex))


    @staticmethod
    def login(data):
        try:
            seller = SellerModel.query.filter_by(email=data["email"]).first()
            if seller and check_password_hash(seller.password, data["password"]):
               return AuthManager.encode_token(seller)
            raise Exception
        except Exception:
            raise BadRequest("Invalid email or password")







class UserManager:


    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"], method="sha256")
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
            return AuthManager.encode_token(user)
        except Exception as ex:
            raise BadRequest(str(ex))


    @staticmethod
    def login(data):
        try:
            user = UserModel.query.filter_by(email=data["email"]).first()
            if user and check_password_hash(user.password, data["password"]):
               return AuthManager.encode_token(user)
            raise Exception
        except Exception:
            raise BadRequest("Invalid email or password")