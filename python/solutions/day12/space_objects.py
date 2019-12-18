import collections
import copy
import itertools
from .algebra import three_way_lcm


class SpaceObject:
    def __init__(self, position):
        self.position = position
        self.velocity = Coord((0, 0, 0))

    def get_potential_energy(self):
        return sum([abs(z) for z in self.position])
    
    def get_kinetic_energy(self):
        return sum([abs(z) for z in self.velocity])

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()

    def __repr__(self):
        return f'<SpaceObject(position={self.position}, velocity={self.velocity})>'


class SpaceObjectSystem:
    def __init__(self, space_objects):
        self.space_objects = space_objects
        self.current_step = 0

    def apply_time_step(self):
        self.apply_time_steps(1)

    def apply_time_steps(self, num):
        for _ in range(num):
            self._apply_gravity()
            self._apply_velocity()
            self.current_step += 1

    def get_total_energy(self):
        return sum([z.get_total_energy() for z in self.space_objects])
        
    def _apply_gravity(self):
        gravity = collections.defaultdict(list)

        for x, y in itertools.combinations(self.space_objects, 2):
            gravity[x].append(-1 * (x.position - y.position).get_unit_vec())
            gravity[y].append(-1 * (y.position - x.position).get_unit_vec())

        for space_object in self.space_objects:
            space_object.velocity += sum(gravity[space_object])

    def _apply_velocity(self):
        for space_object in self.space_objects:
            space_object.position += space_object.velocity


class Coord(tuple):
    def get_unit_vec(self):
        return Coord(x != 0 and int(x / abs(x)) or 0 for x in self)

    def __add__(self, other):
        if isinstance(other, Coord):
            if len(self) != len(other):
                raise ValueError('Coord instances of different lengths cannot be added')
            return Coord(map(sum, zip(self, other)))
        elif isinstance(other, int) and other == 0:
            # So we can use sum() without needing to specify a Coord default start value
            return self
        else:
            raise TypeError(f'Add not implemented for types Coord and {type(other)}')

    def __radd__(self, other):
        return Coord.__add__(self, other) 

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Coord instances of different lengths cannot be subtracted')

        negated_other = Coord(-1 * x for x in other)
        return self + negated_other

    def __rmul__(self, other):
        if isinstance(other, int):
            return Coord((other * z for z in self))

    def __repr__(self):
        return f'<Coord({super().__repr__()})>'


def find_earliest_repetition_of_system_state(space_objects):
    def _get_pos_dim(system, dimension):
        return [obj.position[dimension] for obj in system.space_objects]

    def _get_vel_dim(system, dimension):
        return [obj.velocity[dimension] for obj in system.space_objects]

    # Find out how often each set of coordinates repeats.
    x_period, y_period, z_period = None, None, None
    system = SpaceObjectSystem(copy.deepcopy(space_objects))

    x_pos_initial, x_vel_initial = _get_pos_dim(system, 0), _get_vel_dim(system, 0)
    y_pos_initial, y_vel_initial = _get_pos_dim(system, 1), _get_vel_dim(system, 1)
    z_pos_initial, z_vel_initial = _get_pos_dim(system, 2), _get_vel_dim(system, 2)

    while x_period is None or y_period is None or z_period is None:
        system.apply_time_step()

        if _get_pos_dim(system, 0) == x_pos_initial and _get_vel_dim(system, 0) == x_vel_initial and x_period is None:
            x_period = system.current_step
        if _get_pos_dim(system, 1) == y_pos_initial and _get_vel_dim(system, 1) == y_vel_initial and y_period is None:
            y_period = system.current_step
        if _get_pos_dim(system, 2) == z_pos_initial and _get_vel_dim(system, 2) == z_vel_initial and z_period is None:
            z_period = system.current_step

    return three_way_lcm(x_period, y_period, z_period)
