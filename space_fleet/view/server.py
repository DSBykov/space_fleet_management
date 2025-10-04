from flask import Flask, request
from marshmallow import ValidationError

from space_fleet.business_logic.mission import Mission
from space_fleet.business_logic.spaceship import Spaceship
from space_fleet.data_access.mission_repo import MissionData
from space_fleet.view.mission_schemas import MissionGetManyParamsSchema, MissionHttpDto, MissionCreateSchema, \
    MissionAddSpaceshipSchema
from space_fleet.view.spaceship_schemas import SpaceshipGetManyParamsSchema, SpaceshipHttpDto, SpaceshipCreateSchema, \
    SpaceshipChangeStatusSchema, SpaceshipGetByIdSchema
from space_fleet.data_access.spaceship_repo import SpaceshipData

app = Flask(__name__)

@app.route('/api/v1', methods=['GET'])
def home():
    return "Сервер работает!", 200


# Ендпоинти для управления караблями

# Получение списка всех кораблей.
@app.get('/api/v1/spaceships')
def spaceship_get_many_controller():
    try:
        params = SpaceshipGetManyParamsSchema().load(request.args)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400
    page = params['page']
    limit = params['limit']

    spaceships = SpaceshipData.get_many(page, limit)
    return SpaceshipHttpDto(many=True).dump(spaceships)

# Добавление нового корабля.
@app.post('/api/v1/spaceship')
def spaceship_create_controller():
    try:
        dto = SpaceshipCreateSchema().load(request.json)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400

    spaceship = Spaceship(**dto)
    SpaceshipData.save(spaceship)

    return {
        "status": "Success"
    }, 201

# Обновление статуса корабля.
@app.patch('/api/v1/spaceship')
def spaceship_change_status_controller():
    try:
        params = SpaceshipChangeStatusSchema().load(request.json)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400

    spaceship_id = params['spaceship_id']
    new_spaceship_status = params['status']

    spaceship = SpaceshipData.get_by_id(spaceship_id)
    if spaceship is None:
        return {
            "error": f"Spaceship with id= {spaceship_id} is not found."
        }, 404
    else:
        spaceship.update_status(new_spaceship_status)

    return SpaceshipHttpDto().dump(spaceship)

# Удаление корабля.
@app.delete('/api/v1/spaceship')
def spaceship_delete_controller():
    try:
        params = SpaceshipGetByIdSchema().load(request.json)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400

    print(params)
    spaceship = SpaceshipData.get_by_id(params["spaceship_id"])
    if spaceship is None:
        return {"message": "No Content"}, 204

    print("Start remove")
    SpaceshipData.remove(spaceship)
    print("End remove")
    return {"status": "success"}

# Эндпоинты миссий:

# Получение списка всех миссий.
@app.get('/api/v1/missions')
def mission_get_many_controller():
    try:
        params = MissionGetManyParamsSchema().load(request.args)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400
    page = params['page']
    limit = params['limit']

    missions = MissionData.get_many(page, limit)
    return MissionHttpDto(many=True).dump(missions)


# Создание новой миссии.
@app.post('/api/v1/mission')
def mission_create_controller():
    try:
        dto = MissionCreateSchema().load(request.json)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400

    mission = Mission(**dto)
    MissionData.save(mission)

    return {
        "status": "Success"
    }, 201

# Добавление корабля к миссии.
@app.patch('/api/v1/mission')
def mission_add_spaceship_controller():
    try:
        dto = MissionAddSpaceshipSchema().load(request.json)
    except ValidationError as err:
        return {
            "error": err.messages
        }, 400

    mission = MissionData.get_by_id(dto['mission_id'])
    if mission is None:
        return {
            "error": f"Mission with id= {dto['mission_id']} is not found."
        }, 404

    spaceship = SpaceshipData.get_by_id(dto['spaceship_id'])
    if spaceship is None:
        return {
            "error": f"Spaceship with id= {dto['spaceship_id']} is not found."
        }, 404

    mission.add_spaceship(spaceship)
    return MissionHttpDto().dump(mission)