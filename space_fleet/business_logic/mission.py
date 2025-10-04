from dataclasses import dataclass
from typing import List
from uuid import uuid4

from space_fleet.business_logic.spaceship import Spaceship


@dataclass()
class Mission:
    def __init__(self, name: str,
                 goal: str,
                 status: str = "planned"):
        self.mission_id: str = str(uuid4())
        self.name = name
        self.goal = goal  # исследование или защита (research or protection)
        self.status = status  # запланирована, в процессе, завершена (planned, in progress, completed)
        self.spaceships: List[Spaceship] = []

    def add_spaceship(self, spaceship: Spaceship):
        self.spaceships.append(spaceship)

    def __repr__(self) -> str:
        return f"Mission: '{self.name}' {self.status}, goal: - '{self.goal}'. "\
               f"\nSpaceships: \n\t{'; \n\t'.join([str(s) for s in self.spaceships])}"