from collections.abc import Callable

from src.geometry.primitive import Primitive
from src.hit import Hit
from src.ray import Ray


class World:
    def __init__(self, primitives: list[Primitive] = [], material_fn: Callable | None = None):
        self.primitives = primitives
        self.material_fn = material_fn

    def intersect(self, ray: Ray, hit: Hit | None = None) -> Hit | None:
        for primitive in self.primitives:
            hit = primitive.intersect(ray, hit)
        return hit
