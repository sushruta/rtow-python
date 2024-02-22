from collections.abc import Callable

from src.geometry.primitive import Primitive
from src.hit import Hit
from src.material import Material
from src.ray import Ray


class World:
    def __init__(self, primitives: list[Primitive] = [], material: Material | None = None):
        self.primitives = primitives
        self.material = material

    def intersect(self, ray: Ray, hit: Hit | None) -> Hit | None:
        for primitive in self.primitives:
            if new_hit := primitive.intersect(ray, hit):
                hit = new_hit
        return hit
