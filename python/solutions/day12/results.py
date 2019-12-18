import copy
from .space_objects import Coord, find_earliest_repetition_of_system_state, SpaceObject, SpaceObjectSystem


if __name__ == '__main__':
    # This is the puzzle input
    initial_state = [
        SpaceObject(Coord((-7, -8, 9))),
        SpaceObject(Coord((-12, -3, -4))),
        SpaceObject(Coord((6, -17, -9))),
        SpaceObject(Coord((4, -10, -6))),
    ]

    system = SpaceObjectSystem(copy.deepcopy(initial_state))

    system.apply_time_steps(1000)
    print(f'Part 1:  {system.get_total_energy()}')
    print(f'Part 2:  {find_earliest_repetition_of_system_state(initial_state)}')
