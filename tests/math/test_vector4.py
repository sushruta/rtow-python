import pytest
from pytest_factoryboy import LazyFixture

from src.math.vector4 import Vector4


@pytest.fixture()
def origin():
    return Vector4(0, 0, 0, 0)


@pytest.fixture()
def xaxis():
    return Vector4(1, 0, 0, 0)


@pytest.fixture()
def yaxis():
    return Vector4(0, 1, 0, 0)


@pytest.fixture()
def zaxis():
    return Vector4(0, 0, 1, 0)


@pytest.fixture()
def waxis():
    return Vector4(0, 0, 0, 1)


@pytest.fixture()
def eye():
    return Vector4(1.0, 1.0, 1, 1)


def test_negation():
    v1 = Vector4(1.0, -2.0, 3.0, 1.0)
    v2 = Vector4(-1.0, 2.0, -3.0, -1)
    assert v1 == -v2


def test_inplace_multiplation_float():
    v1 = Vector4(1.0, 2.0, 0.0, 1.0)
    v2 = Vector4(3.0, 6.0, 0.0, 3.0)
    v1 *= 3
    assert v1 == v2


def test_inplace_multiplation_vec():
    v1 = Vector4(1.0, 2.0, 1.0, 1.0)
    v2 = Vector4(3.0, 6.0, 0.0, 1.0)
    v3 = Vector4(3.0, 12.0, 0.0, 1.0)
    assert v1.mul(v2) == v3


def test_multiplication():
    v1 = Vector4(1.0, 2.0, 3.0, 1.0)
    factor = 3.0
    v2 = Vector4(3.0, 6.0, 9.0, 3.0)
    assert v1 * factor == v2
    # also test if it is commutative
    assert factor * v1 == v2


@pytest.mark.parametrize(
    ("lazy_u", "lazy_v", "expected_dot_product"),
    [
        (LazyFixture("xaxis"), LazyFixture("xaxis"), 1.0),
        (LazyFixture("xaxis"), LazyFixture("yaxis"), 0.0),
        (LazyFixture("xaxis"), LazyFixture("eye"), 1.0),
        (LazyFixture("eye"), LazyFixture("zaxis"), 1.0),
        (LazyFixture("eye"), LazyFixture("eye"), 4.0),
    ],
)
def test_dot_product(request, lazy_u, lazy_v, expected_dot_product):
    u = lazy_u.evaluate(request)
    v = lazy_v.evaluate(request)
    actual_dot_product = u.dot(v)
    assert actual_dot_product == expected_dot_product
