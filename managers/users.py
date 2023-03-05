from werkzeug.security import generate_password_hash, check_password_hash
from passlib.hash import sha256_crypt
from werkzeug.exceptions import BadRequest
from models.auth import AuthManager
from models.seller import SellerModel
from db import db


class SellerManager():


    @staticmethod
    def register(seller_data):
        seller_data["password"] = generate_password_hash(seller_data["password"], method="sha256")
        seller = SellerModel(**seller_data)
        try:
            db.session.add(seller)
            db.session.flush()
            return AuthManager.encode_token(seller)
        except Exception as ex:
            raise BadRequest(str(ex))


    @staticmethod
    def login(data):
        try:
            seller = SellerModel.querry.filter_by(email = data["email"]).first()
            if seller and check_password_hash(seller.password, data["password"]):
               return AuthManager.encode_token(seller)
            raise Exeption
        except Exception:
            raise BadRequest("Invalid email or password")
