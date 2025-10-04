from dataclasses import dataclass
from uuid import uuid4


@dataclass()
class Spaceship:
    def __init__(self,
                 name: str,
                 type_: str,
                 status: str = "available"):
        self.spaceship_id: str = str(uuid4())
        self.name = name
        self.type_ = type_  # research or combat
        self.status = status  # available, on mission, under repair

    def update_status(self, new_status: str):
        self.status = new_status

    def __repr__(self) -> str:
        return f'"{self.name}" is {self.type_} spaceship, status: {self.status}'