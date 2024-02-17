from typing import Protocol

# from __future__ import annotations


class Vector(Protocol):
    def __add__(self, other: "Vector") -> "Vector": ...
    def __neg__(self) -> "Vector": ...
    def __mul__(self, factor: float) -> "Vector": ...
    def __rmul__(self, factor: float) -> "Vector": ...
    def __truediv__(self, factor: float) -> "Vector": ...
    def __pos__(self) -> "Vector": ...
    def __sub__(self, other: "Vector") -> "Vector": ...
    def __iadd__(self, other: "Vector") -> "Vector": ...
    def __isub__(self, other: "Vector") -> "Vector": ...
    def __imul__(self, factor: float) -> "Vector": ...
    def __idiv__(self, factor: float) -> "Vector": ...
    def mul(self, other: "Vector") -> "Vector": ...
    def dot(self, other: "Vector") -> float: ...
    def length_squared(self) -> float: ...
    def length(self) -> float: ...
    def unit(self) -> "Vector": ...
    def __str__(self) -> str: ...
