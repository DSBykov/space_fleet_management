from dataclasses import dataclass
from uuid import uuid4

@dataclass()
class CrewMember:
    def __init__(self, name: str, role: str):
        self.member_id: str = str(uuid4())
        self.name = name
        self.role = role  # капитан, инженер или пилот (captain, engineer or pilot)

    def __repr__(self):
        return f'{self.role} - {self.name}'