from marshmallow import Schema, fields
from marshmallow_enum import EnumField
from models.enum import PurchaseState
from models.product import ProductModel




class BaseProductSchema(Schema):
    product_name = fields.String(required=True)
    photo_url = fields.String(required=True)
    amount = fields.Float(required=True)




class RequestProductSchema(BaseProductSchema):
    pass




class ResponseProductSchema(BaseProductSchema):
    id = fields.Integer(required=True)
    status = EnumField(PurchaseState, by_value=True)
    create_on = fields.DateTime(required=True)