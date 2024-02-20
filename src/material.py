from typing import Protocol

from src.math import Vector4
from src.math.vector3 import Vector3
from src.types import Color


class Material(Protocol):
    def shade(self, **kwargs) -> Color: ...


class ConstantColorMaterial:
    def shade(self, **kwargs) -> Color:
        if "hit" in kwargs and kwargs["hit"].normal:
            raise KeyError("hit defined with a valid normal. This is unexpected!")
        return Vector4(1, 0, 0, 1)


class SkyGradientMaterial:
    def shade(self, **kwargs) -> Color:
        if "ray" not in kwargs:
            raise KeyError("ray not found. This is unexpected!")
        ray = kwargs["ray"]
        ud = ray.direction.unit()
        factor = 0.5 * (ud.y + 1)
        return Vector4(1 - 0.5 * factor, 1 - 0.3 * factor, 1, 1)


class NormalDirectionMaterial:
    def shade(self, **kwargs) -> Color:
        if "normal" not in kwargs:
            raise KeyError("hit should be defined with a valid normal")
        match kwargs["normal"]:
            case Vector3(x, y, z):
                return 0.5 * Vector4(x + 1, y + 1, z + 1, 2)
            case _:
                raise KeyError("hit should be defined with a valid normal")
