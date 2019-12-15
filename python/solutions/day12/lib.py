import collections
import itertools


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

    def apply_time_step(self):
        self._apply_gravity()
        self._apply_velocity()

    def apply_time_steps(self, num):
        for _ in range(num):
            self.apply_time_step()

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
