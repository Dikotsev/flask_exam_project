from db import db
from models.product import ProductModel
from models.enum import PurchaseState



class ProductManager:


    @staticmethod
    def get_all_products():
        if instance(user, SellerModel):
            return ProductModel.query.filter_by(seller_id=user.id).all()
        return ProductModel.query.all()


    @staticmethod
    def add_product(data, seller_id):
        data["seller_id"] = seller_id
        product = ProductModel(**data)
        db.add(product)
        db.commit()
        return product


    @staticmethod
    def approve_purchase(id_):
        ProductModel.query.filter_by(id=id_).update({"status": PurchaseState.pending})



    @staticmethod
    def rejected_purchase(id_):
        ProductModel.query.filter_by(id=id_).update({"status": PurchaseState.rejected})


    @staticmethod
    def completed_purchase(id_):
        ProductModel.query.filter_by(id=id_).update({"status": PurchaseState.completed})