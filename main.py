from space_fleet.business_logic.spaceship import Spaceship
from space_fleet.business_logic.mission import Mission
from space_fleet.business_logic.crew_member import CrewMember


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    milano = Spaceship(name = 'Milano',
                       type_ = 'research')
    print(milano)

    infinity_stones = Mission(name='Infinity Stones',
                              goal='research')

    print(infinity_stones)

    piter_quill = CrewMember(name='Piter Quill', role='captain')

    print(piter_quill)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
