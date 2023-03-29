from flask_restful import Resource
from flask import request
from db import db
from models.enum import UserRolesEnum, PurchaseState
from managers.product_manager import ProductManager
from models.product import ProductModel
from models.auth import auth
from schemas.decorator import validate_schema, permission_required
from schemas.product_schema import ResponseProductSchema, RequestProductSchema




class ProductList(Resource):


    @auth.login_required
    @validate_schema(RequestProductSchema)
    def get(self):
        user = auth.current_user()
        products = ProductManager.get_all_products(user)
        return ResponseProductSchema().dump(products)



    @auth.login_required
    @permission_required(UserRolesEnum.seller)
    @validate_schema(RequestProductSchema)
    def post(self):
        seller = auth.current_user()
        data = request.get_json()
        product = ProductManager.add_product(data, seller.id)
        return ResponseProductSchema().dump(product)




class ApproveProductPurchase(Resource):
    @auth.login_required
    @permission_required(UserRolesEnum.admin)
    def put(self, id_):
        ProductManager.approve_purchase(id_)
        return 200




class RejectProductPurchase(Resource):
    @auth.login_required
    @permission_required(UserRolesEnum.admin)
    def delete(self, id_):
        ProductManager.rejected_purchase(id_)
        return 200
