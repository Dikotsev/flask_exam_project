from sqlalchemy import func
from db import db

from models.enum import PurchaseState



class ProductModel(db.Model):

    __tablename__ = "products"


    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    purchase_status = db.Column(
        db.Enum(PurchaseState),
        default=PurchaseState.listed,
        nullable=False
    )
    seller_id = db.Column(db.Integer, db.ForeignKey("sellers.id"))
    seller = db.relationship("SellerModel")

