from typing import Protocol

from src.hit import Hit
from src.ray import Ray
from src.types import Color


class Primitive(Protocol):
    def intersect(self, ray: Ray, hit: Hit | None = None) -> Hit | None: ...
    def color(self, ray: Ray) -> Color: ...
