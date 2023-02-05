from db import db

from models.enum import UserRolesEnum
from models.user import BaseUserModel

class AdminModel(BaseUserModel):
     __tablename__ = "admins"
     __table_args__ = {'extend_existing': True}
     __mapper_args__ = {
         'polymorphic_identity': 'admins',
         'inherit_condition': (id == BaseUserModel.id),
     }

#     id = db.Column(db.Integer, primary_key=True)
     role = db.Column(
                  db.Enum(UserRolesEnum),
                  default=UserRolesEnum.admin,
                  nullable=False
                  )
