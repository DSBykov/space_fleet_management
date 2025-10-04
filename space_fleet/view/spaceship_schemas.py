from marshmallow import Schema, fields
from marshmallow.validate import OneOf

_available_statuses = ["available", "on mission", "under repair"]
_available_types = ["research", "combat"]

class SpaceshipGetByIdSchema(Schema):
    spaceship_id = fields.Str(required=True)

class SpaceshipChangeStatusSchema(Schema):
    spaceship_id = fields.Str(required=True)
    status = fields.Str(validate=OneOf(_available_statuses), required=True)

class SpaceshipCreateSchema(Schema):
    name = fields.Str(required=True)
    type_= fields.Str(required=True, validate=OneOf(_available_types))
    status = fields.Str(validate=OneOf(_available_statuses))

class SpaceshipGetManyParamsSchema(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)


class SpaceshipHttpDto(Schema):
    class Meta:
        fields = ["spaceship_id", "name", "type_", "status"]

    spaceship_id = fields.Str(required=True)
    name = fields.Str(required=True)
    type_ = fields.Str(required=True)
    status = fields.Str(required=True)