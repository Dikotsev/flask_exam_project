from marshmallow import Schema, fields


class UserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)


class UserRegisterSchema(UserSchema):
    name = fields.String(min_length=2, required=True)
    phone = fields.String(max_length=12, required=True)


class UserLoginSchema(UserSchema):
#  email = fields.Email(load_from="email" ,dump_to="email")
   pass