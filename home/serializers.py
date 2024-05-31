from marshmallow import Schema, fields, validate


class EventSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    date = fields.Date()
