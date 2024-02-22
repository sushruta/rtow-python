import dataclasses
from collections.abc import Callable

from src.math import Vector3
from src.ray import Ray
from src.types import Point3


@dataclasses.dataclass()
class Hit:
    ray: Ray
    t: float
    material_fn: Callable | None = None
    normal: Vector3 | None = None

    @property
    def point(self) -> Point3:
        return self.ray.at(self.t)
