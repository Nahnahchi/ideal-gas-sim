from random import random
from mpl_toolkits import mplot3d
from matplotlib import pyplot


delta_t = 0.001
num_part = 100
num_steps = 10000


class Box:

    def __init__(self, width: int, height: int, length: int):
        self.width = width
        self.height = height
        self.length = length
        self.molecules = []

    def fill(self, num: int):
        rnd = lambda l: random()*l - 0.5*l
        for _ in range(num):
            mol = Molecule(
                            coordinates={
                                'x': random() * self.width / 2,
                                'y': rnd(self.height),
                                'z': rnd(self.length)
                            },
                            velocities={
                                'x': rnd(self.width),
                                'y': rnd(self.height),
                                'z': rnd(self.length)
                            }
            )
            self.molecules.append(mol)

    def simulate(self):
        for _ in range(num_steps):
            for mol in self.molecules:
                mol.move()
                if abs(mol.get_x() + mol.get_dx() * delta_t) >= self.width / 2:
                    mol.bounce(axis='x')
                if abs(mol.get_y() + mol.get_dy() * delta_t) >= self.height / 2:
                    mol.bounce(axis='y')
                if abs(mol.get_z() + mol.get_dz() * delta_t) >= self.length / 2:
                    mol.bounce(axis='z')


class Molecule:

    def __init__(self, coordinates: dict, velocities: dict):
        self.coordinates = coordinates
        self.velocities = velocities

    def get_x(self):
        return self.coordinates['x']

    def get_y(self):
        return self.coordinates['y']

    def get_z(self):
        return self.coordinates['z']

    def get_dx(self):
        return self.velocities['x']

    def get_dy(self):
        return self.velocities['y']

    def get_dz(self):
        return self.velocities['z']

    def move(self):
        for axis in self.coordinates.keys():
            self.coordinates[axis] += self.velocities[axis] * delta_t

    def bounce(self, axis: str):
        self.velocities[axis] = -self.velocities[axis]


if __name__ == '__main__':

    box = Box(2, 2, 2)
    box.fill(num_part)
    box.simulate()

    X = [x.get_x() for x in box.molecules]
    Y = [y.get_y() for y in box.molecules]
    Z = [z.get_z() for z in box.molecules]

    fig = pyplot.figure()
    ax = pyplot.axes(projection='3d')
    ax.scatter3D(X, Y, Z, c=Z, cmap='Greens')
    pyplot.show()
