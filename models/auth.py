
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta
from decouple import config
from werkzeug.exceptions import BadRequest, Unauthorized
from werkzeug.exceptions import Unauthorized
from flask_httpauth import HTTPTokenAuth
from models.user import UserModel


auth = HTTPTokenAuth(scheme='Bearer')



@auth.verify_token
def verify_token(token):
    try:
        user_id = AuthManager.decode_token(token)
        return UserModel.query.filter_by(id=user_id).first()
    except Unauthorized as ex:
        return ex("Invalid or missing token"), 400


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            payload = {
            'exp': datetime.utcnow() + timedelta(days=2),
            'sub': user.id,
            'type': user.__class__.__name__
                    }
            return jwt.encode(
                    payload,
                    key=config('SECRET_KEY'),
                    algorithm='HS256'
        )
        except Exception as e:
            raise e

    @staticmethod
    def decode_token(token):
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise Unauthorized("Token expired")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


