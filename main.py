from space_fleet.business_logic.spaceship import Spaceship
from space_fleet.business_logic.mission import Mission
from space_fleet.business_logic.crew_member import CrewMember
from space_fleet.data_access.mission_repo import MissionData
from space_fleet.data_access.spaceship_repo import SpaceshipData

from space_fleet.view.server import app

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    milano = Spaceship(name = 'Milano', type_ = 'research')
    SpaceshipData.save(milano)
    infinity_stones = Mission(name='Infinity Stones', goal='research')
    MissionData.save(infinity_stones)
    piter_quill = CrewMember(name='Piter Quill', role='captain')

    app.run(port=5000, debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
