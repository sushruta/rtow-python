import math
from collections.abc import Callable

from src.hit import Hit
from src.math.vector3 import Vector3
from src.ray import Ray


def get_closest_hit(h1: Hit | None, h2: Hit | None) -> Hit | None:
    match h1, h2:
        case (None, None):
            return None
        case (_, None):
            return h1
        case (None, _):
            return h2
    assert h1
    assert h2
    if h1.t < 0 and h2.t < 0:
        return None
    if h1.t < 0:
        return h2
    if h2.t < 0:
        return h1
    return h1 if h1.t < h2.t else h2


class Sphere:
    def __init__(self, center: Vector3, radius: float, material_fn: Callable | None = None):
        self.center = center
        self.radius = radius
        self.material_fn = material_fn

    def intersect(self, ray: Ray, hit: Hit | None = None) -> Hit | None:
        oc = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius

        disc = b * b - 4 * a * c
        if disc < 0:
            return None
        t1 = (-b - math.sqrt(disc)) / (2 * a)
        t2 = (-b + math.sqrt(disc)) / (2 * a)

        hit1 = Hit(ray, t1)
        hit2 = Hit(ray, t2)

        final_hit = get_closest_hit(hit, get_closest_hit(hit1, hit2))
        if not final_hit:
            return None
        final_hit.normal = (ray.at(final_hit.t) - self.center).unit()
        final_hit.material_fn = self.material_fn
        return final_hit
