import math

import pytest
from pytest_factoryboy import LazyFixture

from src.math.vector2 import Vector2


@pytest.fixture()
def vec1():
    return Vector2(0.0, 0.0)


@pytest.fixture()
def vec2():
    return Vector2(1.0, 0.0)


@pytest.fixture()
def vec3():
    return Vector2(0.0, 1.0)


@pytest.fixture()
def vec4():
    return Vector2(1.0, 1.0)


def test_negation():
    v1 = Vector2(1.0, -2.0)
    v2 = Vector2(-1.0, 2.0)
    assert v1 == -v2


def test_inplace_multiplation_float():
    v1 = Vector2(1.0, 2.0)
    v2 = Vector2(3.0, 6.0)
    v1 *= 3
    assert v1 == v2


def test_inplace_multiplation_vec():
    v1 = Vector2(1.0, 2.0)
    v2 = Vector2(3.0, 6.0)
    v3 = Vector2(3.0, 12.0)
    assert v1.mul(v2) == v3


def test_multiplication():
    v1 = Vector2(1.0, 2.0)
    factor = 3.0
    v2 = Vector2(3.0, 6.0)
    assert v1 * factor == v2
    # also test if it is commutative
    assert factor * v1 == v2


@pytest.mark.parametrize(
    ("lazy_u", "lazy_v", "expected_dot_product"),
    [
        (LazyFixture("vec1"), LazyFixture("vec3"), 0.0),
        (LazyFixture("vec3"), LazyFixture("vec3"), 1.0),
        (LazyFixture("vec1"), LazyFixture("vec4"), 0.0),
        (LazyFixture("vec4"), LazyFixture("vec2"), 1.0),
        (LazyFixture("vec4"), LazyFixture("vec4"), 2.0),
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
        (LazyFixture("vec1"), LazyFixture("vec3"), Vector2(0.0, 1.0)),
        (LazyFixture("vec4"), LazyFixture("vec4"), Vector2(2.0, 2.0)),
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
        (LazyFixture("vec1"), 0.0),
        (LazyFixture("vec2"), 1.0),
        (LazyFixture("vec3"), 1.0),
        (LazyFixture("vec4"), math.sqrt(2.0)),
    ],
)
def test_length(request, lazy_u, expected_length):
    u = lazy_u.evaluate(request)
    actual_length = u.length()
    assert actual_length == expected_length
