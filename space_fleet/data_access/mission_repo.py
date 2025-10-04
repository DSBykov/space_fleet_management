from typing import List, Optional
from space_fleet.business_logic.mission import Mission

_missions: List[Mission] = []

class MissionData:
    @staticmethod
    def save(mission: Mission):
        for i in range(len(_missions)):
            existed_mission = _missions[i]
            if existed_mission.mission_id == mission.mission_id:
                _missions[i] = mission
                break
        else:
            _missions.append(mission)


    @staticmethod
    def get_by_id(id: str) -> Optional[Mission]:
        return next((m for m in _missions if m.mission_id == id), None)


    @staticmethod
    def get_many(page: int = 0, limit: int = 10):
        start = page * limit
        end = start + limit
        return _missions[start:end]


    @staticmethod
    def remove(mission: Mission):
        _missions.remove(mission)
