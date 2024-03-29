import math
from collections.abc import Callable

from src.hit import Hit
from src.material import Material
from src.math.vector3 import Vector3
from src.ray import Ray


def get_closest_hit(h1: Hit | None, h2: Hit | None) -> Hit | None:
    if not h1 and not h2:
        return None
    if not h1:
        return h2
    if not h2:
        return h1
    assert h1
    assert h2
    return h1 if h1.t < h2.t else h2


class Sphere:
    def __init__(self, center: Vector3, radius: float, material: Material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersect(self, ray: Ray, hit: Hit | None) -> Hit | None:
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius

        disc = b * b - 4 * a * c
        if disc < 0:
            return None
        t1 = (-b - math.sqrt(disc)) / (2 * a)
        t2 = (-b + math.sqrt(disc)) / (2 * a)

        hit1 = (
            Hit(ray, t1, self.material.shade, (ray.at(t1) - self.center).unit())
            if t1 >= 0
            else None
        )
        hit2 = (
            Hit(ray, t2, self.material.shade, (ray.at(t2) - self.center).unit())
            if t2 >= 0
            else None
        )

        final_hit = get_closest_hit(hit, get_closest_hit(hit1, hit2))
        if not final_hit:
            return None
        return final_hit
