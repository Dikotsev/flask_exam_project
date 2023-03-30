from db import db

from models.enum import UserRolesEnum
from models.user import BaseUserModel


class SellerModel(BaseUserModel):
     __tablename__ = "sellers"
     __table_args__ = {'extend_existing': True}
     __mapper_args__ = {
         'polymorphic_identity': 'sellers',
         'inherit_condition': (id == BaseUserModel.id),
     }

#    id = db.Column(db.Integer, primary_key=True)
     role = db.Column(
                  db.Enum(UserRolesEnum),
                  default=UserRolesEnum.seller,
                  nullable=False
                  )
     products = db.relationship("ProductModel", backref="products", lazy="dynamic")
