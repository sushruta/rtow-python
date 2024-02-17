from tqdm import tqdm

from src.camera import SimpleCamera
from src.math.vector4 import Vector4
from src.types import Color


def write_color(color: Color, flw) -> None:
    ir = int(255.999 * color.x)
    ig = int(255.999 * color.y)
    ib = int(255.999 * color.z)

    line = f"{ir} {ig} {ib}"
    match flw:
        case None:
            raise AttributeError("please provide valid file")
        case _:
            flw.write(f"{line}\n")


def create_simple_image():
    aspect_ratio = 16.0 / 9.0
    image_width = 400
    image_height = int(image_width / aspect_ratio)

    camera = SimpleCamera(aspect_ratio, image_width)

    with open("out.ppm", "w") as flw:
        flw.write(f"P3\n{image_width} {image_height}\n255\n")

        for h in tqdm(range(image_height)):
            for w in range(image_width):
                ray = camera.generate_ray(w, h)

                unit_direction = ray.direction.unit()
                factor = 0.5 * (unit_direction.y + 1.0)

                r = 1.0 - 0.5 * factor
                g = 1.0 - 0.3 * factor
                b = 1.0

                color = Vector4(r, g, b, 1.0)
                write_color(color, flw)
