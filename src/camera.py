import math
from typing import Protocol

from src.math import Vector3
from src.ray import Ray
from src.types import Point3


class Camera(Protocol):
    def generate_ray(self, x: float, y: float) -> Ray: ...


# Following assumptions are made -
# focal length : 1.0
# viewport height : 2.0
# viewport width : viewport_height * aspect_ratio
class SimpleCamera:
    def __init__(self, aspect_ratio: float, image_width: int):
        if image_width == 0:
            raise ValueError("image width can not be zero")
        if math.isclose(aspect_ratio, 0.0):
            raise ValueError("aspect ratio can not be zero")
        image_height = image_width / aspect_ratio
        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * aspect_ratio
        self.camera_center: Point3 = Vector3(0, 0, 0)

        viewport_u = Vector3(viewport_width, 0, 0)
        viewport_v = Vector3(0, -viewport_height, 0)

        self.pixel_delta_u = viewport_u / image_width
        self.pixel_delta_v = viewport_v / image_height

        viewport_upper_left = (
            self.camera_center - Vector3(0, 0, focal_length) - viewport_u * 0.5 - viewport_v * 0.5
        )
        self.pixel_00 = viewport_upper_left + 0.5 * self.pixel_delta_u + 0.5 * self.pixel_delta_v

    def generate_ray(self, x: int, y: int) -> Ray:
        pixel_center = self.pixel_00 + (x * self.pixel_delta_u) + (y * self.pixel_delta_v)
        direction = pixel_center - self.camera_center
        return Ray(self.camera_center, direction)
