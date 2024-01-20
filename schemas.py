from marshmallow import Schema, fields, validate

class FizzBuzzSchema(Schema):
    int1 = fields.Integer(required=True, validate=validate.Range(min=1))
    int2 = fields.Integer(required=True, validate=validate.Range(min=1))
    limit = fields.Integer(required=True, validate=validate.Range(min=1))
    str1 = fields.String(required=True)
    str2 = fields.String(required=True)