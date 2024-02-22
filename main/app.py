from tqdm import tqdm

from src.camera import SimpleCamera
from src.geometry import Sphere, World
from src.material import (
    NormalDirectionMaterial,
    SkyGradientMaterial,
)
from src.math import Vector3, Vector4
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

    normal_material = NormalDirectionMaterial()
    sky_material = SkyGradientMaterial()

    sphere1 = Sphere(Vector3(0, 0, -1), 0.5, normal_material)
    sphere2 = Sphere(Vector3(0, -100.5, -1), 100, normal_material)

    world = World([sphere2, sphere1])
    world.material = sky_material

    with open("out.ppm", "w") as flw:
        flw.write(f"P3\n{image_width} {image_height}\n255\n")

        for h in tqdm(range(image_height)):
            for w in range(image_width):
                ray = camera.generate_ray(w, h)

                color = Vector4(1, 1, 1, 1)

                current_hit = world.intersect(ray, None)
                if current_hit:
                    assert current_hit.material_fn
                    color = current_hit.material_fn(normal=current_hit.normal)
                else:
                    assert world.material
                    color = world.material.shade(ray=ray)

                write_color(color, flw)
