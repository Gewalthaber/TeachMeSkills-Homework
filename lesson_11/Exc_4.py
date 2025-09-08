from math import pi

class Sphere:
    def __init__(self, radius=None, x=None, y=None, z=None):

        if radius is None and x is None and y is None and z is None:
            self.radius = 1.0
            self.center = (0.0, 0.0, 0.0)
        elif x is None and y is None and z is None:
            self.radius = float(radius)
            self.center = (0.0, 0.0, 0.0)
        else:
            self.radius = float(radius)
            self.center = (self.x, self.y, self.z)

    def get_volume(self):
        volume = (4 / 3) * pi * (self.radius ** 3)
        return f"Объем шара: {round(volume, 2)}"

    def get_square(self):
        square = 4 * pi * (self.radius ** 2)
        return f"Площадь внешней поверхности сферы: {round(square, 2)}"

    def get_radius(self):
        return f"Радиус текущей сферы: {self.radius}"

    def get_center(self):
        return f"Кортеж с координатами центра сферы: {self.center}"

    def set_radius(self, radius):
        self.radius = float(radius)

    def set_center(self, x, y, z):
        self.center = (float(x), float(y), float(z))

    def is_point_inside(self, x, y, z):
        cx, cy, cz = self.center
        distance_squared = (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2
        return distance_squared <= self.radius ** 2

sph_1 = Sphere(2, 3, 4, 5)
print(sph_1.get_volume())
print(sph_1.get_square())
print(sph_1.get_radius())
print(sph_1.get_center())
sph_1.set_radius(3)
print(sph_1.get_radius())
sph_1.set_center(1, 2, 3)
print(sph_1.get_center())
print(sph_1.is_point_inside(5, 6, 7))




