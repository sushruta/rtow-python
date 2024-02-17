import pytest

from src.math.vector4 import Vector4
from src.types import Color


@pytest.fixture()
def red() -> Color:
    return Vector4(1, 0, 0, 1)


def test_color_loading(red):
    color = red
    assert color.r == 1
    assert color.g == 0
    assert color.b == 0
    assert color.a == 1
