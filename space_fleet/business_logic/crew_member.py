from dataclasses import dataclass
from uuid import UUID, uuid4

@dataclass()
class CrewMember:
    def __init__(self, name: str, role: str):
        self.member_id: UUID = uuid4()
        self.name = name
        self.role = role  # капитан, инженер или пилот (captain, engineer or pilot)

    def __repr__(self):
        return f'{self.role} - {self.name}'