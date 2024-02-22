from PIL import Image

from src.camera import SimpleCamera
from src.geometry.sphere import Sphere
from src.math.vector3 import Vector3

from src.material import NormalDirectionMaterial


def test_simple_red_sphere():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    png_image = Image.open("tests/files/test_simple_red_sphere.png")
    ew, eh = png_image.size
    assert ew == image_width
    assert eh == image_height

    rgb_im = png_image.convert("RGB")

    sc = SimpleCamera(aspect_ratio, image_width)

    normal_material = NormalDirectionMaterial()
    sphere = Sphere(Vector3(0, 0, -1), 0.5, normal_material)

    ## do a pixel wise comparison of the actual
    ## and the expected image
    for h in range(image_height):
        for w in range(image_width):
            ray = sc.generate_ray(w, h)

            hit = sphere.intersect(ray, None)
            unit_direction = ray.direction.unit()
            f = 0.5 * (unit_direction.y + 1.0)
            ar = int(255.999 * (1.0 - 0.5 * f))
            ag = int(255.999 * (1.0 - 0.3 * f))
            ab = 255
            if hit:
                ar = 255
                ag = 0
                ab = 0

            er, eg, eb = rgb_im.getpixel((w, h))
            assert er == ar
            assert eg == ag
            assert eb == ab
