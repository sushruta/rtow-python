import math

import pytest
from PIL import Image

from src.camera import SimpleCamera
from src.math.vector3 import Vector3


@pytest.mark.parametrize(
    ("aspect_ratio", "image_width", "error_info"),
    [(16.0 / 9.0, 0, "image width can not be zero"), (0.0, 256, "aspect ratio can not be zero")],
)
def test_simplecamera_bad_iw(aspect_ratio, image_width, error_info):
    with pytest.raises(ValueError, match=error_info):
        _ = SimpleCamera(aspect_ratio, image_width)


def test_simplecamera_init():
    aspect_ratio = 16.0 / 9.0
    image_width = 256
    expected_pixel_00 = Vector3(-1.770833333, 0.9930555555, -1)
    sc = SimpleCamera(aspect_ratio, image_width)
    assert sc.camera_center == Vector3(0, 0, 0)
    assert math.isclose(sc.pixel_00.x, expected_pixel_00.x)
    assert math.isclose(sc.pixel_00.y, expected_pixel_00.y)
    assert math.isclose(sc.pixel_00.z, expected_pixel_00.z)


def test_generate_ray():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    png_image = Image.open("tests/files/test_generate_ray.png")
    ew, eh = png_image.size
    assert ew == image_width
    assert eh == image_height

    rgb_im = png_image.convert("RGB")

    sc = SimpleCamera(aspect_ratio, image_width)

    ## do a pixel wise comparison of the actual
    ## and the expected image
    for h in range(image_height):
        for w in range(image_width):
            ray = sc.generate_ray(w, h)
            unit_direction = ray.direction.unit()
            f = 0.5 * (unit_direction.y + 1.0)

            r, g, b = rgb_im.getpixel((w, h))
            assert r == int(255.999 * (1.0 - 0.5 * f))
            assert g == int(255.999 * (1.0 - 0.3 * f))
            assert b == 255
