from PIL import Image


def test_ppm_png_equality(ppm_image_path: str, png_image_path: str) -> bool:
    ppm_image = Image.open(ppm_image_path)
    png_image = Image.open(png_image_path)

    if ppm_image.size != png_image.size:
        return False

    w, h = ppm_image.size

    ppm_pixels = ppm_image.load()
    png_pixels = png_image.load()

    diff_count = 0
    for x in range(ppm_image.width):
        for y in range(ppm_image.height):
            if ppm_pixels[x, y] != png_pixels[x, y]:
                diff_count += 1

    if diff_count > 0.01 * (w * h):
        return False
    return True
