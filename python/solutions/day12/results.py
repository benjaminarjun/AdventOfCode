from .lib import Coord, SpaceObject, SpaceObjectSystem


if __name__ == '__main__':
    system = SpaceObjectSystem([
        SpaceObject(Coord((-7, -8, 9))),
        SpaceObject(Coord((-12, -3, -4))),
        SpaceObject(Coord((6, -17, -9))),
        SpaceObject(Coord((4, -10, -6))),
    ])

    system.apply_time_steps(1000)
    print(f'Part 1:  {system.get_total_energy()}')
