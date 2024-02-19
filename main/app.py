from tqdm import tqdm

from src.camera import SimpleCamera
from src.geometry import Sphere, World
from src.material import shade_normal_direction, shade_sky_gradient
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

    sphere = Sphere(Vector3(0, 0, -1), 0.5)
    sphere.material_fn = shade_normal_direction

    world = World([sphere])
    world.material_fn = shade_sky_gradient

    with open("out.ppm", "w") as flw:
        flw.write(f"P3\n{image_width} {image_height}\n255\n")

        for h in tqdm(range(image_height)):
            for w in range(image_width):
                ray = camera.generate_ray(w, h)

                color = Vector4(1, 1, 1, 1)

                current_hit = world.intersect(ray)
                if current_hit and current_hit.material_fn:
                    color = current_hit.material_fn(hit=current_hit)
                else:
                    color = world.material_fn(ray=ray)

                write_color(color, flw)
