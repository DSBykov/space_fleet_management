from typing import List, Optional

from space_fleet.business_logic.spaceship import Spaceship

_spaceships: List[Spaceship] = []

def save(spaceship: Spaceship):
    for i in range(len(_spaceships)):
        existed_spaceship = _spaceships[i]
        if existed_spaceship.spaceship_id == spaceship.spaceship_id:
            _spaceships[i] = spaceship
            break
    else:
        _spaceships.append(spaceship)

def get_by_id(id: str) -> Optional[Spaceship]:
    return next((s for s in _spaceships if s.spaceship_id == id), None)

def get_many(page: int = 0, limit: int = 10):
    start = page * limit
    end = start + limit
    return _spaceships[start:end]