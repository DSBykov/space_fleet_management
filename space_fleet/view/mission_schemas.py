from marshmallow import Schema, fields
from marshmallow.validate import OneOf
from space_fleet.view.spaceship_schemas import SpaceshipHttpDto

_available_statuses = ["planned", "progress", "completed"]
_available_goals = ["research", "protection"]

class MissionGetByIdSchema(Schema):
    mission_id = fields.Str(required=True)

class MissionChangeStatusSchema(Schema):
    mission_id = fields.Str(required=True)
    status = fields.Str(validate=OneOf(_available_statuses), required=True)

class MissionCreateSchema(Schema):
    name = fields.Str(required=True)
    goal= fields.Str(required=True, validate=OneOf(_available_goals))
    status = fields.Str(validate=OneOf(_available_statuses))

class MissionGetManyParamsSchema(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)

class MissionAddSpaceshipSchema(Schema):
    mission_id = fields.Str(required=True)
    spaceship_id = fields.Str(required=True)

class MissionHttpDto(Schema):
    class Meta:
        fields = ["mission_id", "name", "goal", "status", "spaceships"]

    mission_id = fields.Str(required=True)
    name = fields.Str(required=True)
    goal = fields.Str(required=True, validate=OneOf(_available_goals))
    status = fields.Str(required=True, validate=OneOf(_available_statuses))
    spaceships = fields.List(fields.Nested(SpaceshipHttpDto), required=True)