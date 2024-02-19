from src.math import Vector4
from src.types import Color


def shade_constant_color(**kwargs) -> Color:
    if "hit" in kwargs and kwargs["hit"].normal:
        raise KeyError("hit defined with a valid normal. This is unexpected!")
    return Vector4(1, 0, 0, 1)


def shade_sky_gradient(**kwargs) -> Color:
    if "ray" not in kwargs:
        raise KeyError("ray not found. This is unexpected!")
    ray = kwargs["ray"]
    ud = ray.direction.unit()
    factor = 0.5 * (ud.y + 1)
    return Vector4(1 - 0.5 * factor, 1 - 0.3 * factor, 1, 1)


def shade_normal_direction(**kwargs) -> Color:
    if "hit" not in kwargs or not kwargs["hit"].normal:
        raise KeyError("hit should be defined with a valid normal")
    n = kwargs["hit"].normal
    color = Vector4(n.x + 1, n.y + 1, n.z + 1, 1)
    color *= 0.5
    color.w = 1.0
    return color
