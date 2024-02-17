import dataclasses

from src.hit import Hit
from src.math.vector3 import Vector3
from src.math.vector4 import Vector4
from src.ray import Ray
from src.types import Color


@dataclasses.dataclass()
class Sphere:
    center: Vector3
    radius: float

    def intersect(self, ray: Ray, hit: Hit | None = None) -> Hit | None:
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius

        disc = b * b - 4 * a * c
        if disc > 0:
            return Hit(ray, 0.0)
        return None

    def color(self, hit: Hit) -> Color:
        return Vector4(1.0, 0, 0, 1)
