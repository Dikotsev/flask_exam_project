from db import db

from models.enum import UserRolesEnum




class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(15), nullable=False)


class UserModel(BaseUserModel):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    __mapper_args__ = {
        'polymorphic_identity': 'users',
        'inherit_condition': (id == BaseUserModel.id),
    }

#    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Enum(UserRolesEnum),
                    server_default=UserRolesEnum.user.name,
                    nullable=False
                     )

