import dataclasses

from src.math import Vector3
from src.types import Point3


@dataclasses.dataclass()
class Ray:
    origin: Point3
    direction: Vector3

    def at(self, t: float) -> Point3:
        return self.origin + t * self.direction
