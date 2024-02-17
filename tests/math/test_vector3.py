import math

import pytest
from pytest_factoryboy import LazyFixture

from src.math.vector3 import Vector3


@pytest.fixture()
def origin():
    return Vector3(0, 0, 0)


@pytest.fixture()
def xaxis():
    return Vector3(1, 0, 0)


@pytest.fixture()
def yaxis():
    return Vector3(0, 1, 0)


@pytest.fixture()
def zaxis():
    return Vector3(0, 0, 1)


@pytest.fixture()
def eye():
    return Vector3(1.0, 1.0, 1)


def test_negation():
    v1 = Vector3(1.0, -2.0, 3.0)
    v2 = Vector3(-1.0, 2.0, -3.0)
    assert v1 == -v2


def test_inplace_multiplation_float():
    v1 = Vector3(1.0, 2.0, 0.0)
    v2 = Vector3(3.0, 6.0, 0.0)
    v1 *= 3
    assert v1 == v2


def test_inplace_multiplation_vec():
    v1 = Vector3(1.0, 2.0, 1.0)
    v2 = Vector3(3.0, 6.0, 0.0)
    v3 = Vector3(3.0, 12.0, 0.0)
    assert v1.mul(v2) == v3


def test_multiplication():
    v1 = Vector3(1.0, 2.0, 3.0)
    factor = 3.0
    v2 = Vector3(3.0, 6.0, 9.0)
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
        (LazyFixture("eye"), LazyFixture("eye"), 3.0),
    ],
)
def test_dot_product(request, lazy_u, lazy_v, expected_dot_product):
    u = lazy_u.evaluate(request)
    v = lazy_v.evaluate(request)
    actual_dot_product = u.dot(v)
    assert actual_dot_product == expected_dot_product


@pytest.mark.parametrize(
    ("lazy_u", "lazy_v", "expected_sum"),
    [
        (LazyFixture("xaxis"), LazyFixture("zaxis"), Vector3(1.0, 0.0, 1.0)),
        (LazyFixture("eye"), LazyFixture("zaxis"), Vector3(1.0, 1.0, 2.0)),
    ],
)
def test_sum(request, lazy_u, lazy_v, expected_sum):
    u = lazy_u.evaluate(request)
    v = lazy_v.evaluate(request)
    actual_sum = u + v
    assert actual_sum == expected_sum


@pytest.mark.parametrize(
    ("lazy_u", "expected_length"),
    [
        (LazyFixture("xaxis"), 1.0),
        (LazyFixture("origin"), 0.0),
        (LazyFixture("eye"), math.sqrt(3)),
    ],
)
def test_length(request, lazy_u, expected_length):
    u = lazy_u.evaluate(request)
    actual_length = u.length()
    assert actual_length == expected_length


def test_crossproduct_parallel_vectors(xaxis, origin):
    v1 = xaxis
    v2 = xaxis * 2
    v3 = origin
    assert v1.cross(v2) == v3


def test_maxwell_right_hand_principle(xaxis, yaxis, zaxis, origin):
    assert zaxis == xaxis.cross(yaxis)
    assert -zaxis == yaxis.cross(xaxis)
    assert yaxis == zaxis.cross(xaxis)
    assert zaxis.cross(zaxis) == origin
