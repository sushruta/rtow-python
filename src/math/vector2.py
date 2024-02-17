import dataclasses
import math


@dataclasses.dataclass()
class Vector2:
    x: float
    y: float

    def __add__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x + other.x, self.y + other.y)

    def __neg__(self) -> "Vector2":
        return Vector2(-self.x, -self.y)

    def __mul__(self, factor: float) -> "Vector2":
        return Vector2(self.x * factor, self.y * factor)

    def __rmul__(self, factor: float) -> "Vector2":
        return self * factor

    def __truediv__(self, factor: float) -> "Vector2":
        return Vector2(self.x / factor, self.y / factor)

    def __pos__(self) -> "Vector2":
        return self

    def __sub__(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x - other.x, self.y - other.y)

    def __iadd__(self, other: "Vector2") -> "Vector2":
        return self + other

    def __isub__(self, other: "Vector2") -> "Vector2":
        return self - other

    def __imul__(self, factor: float) -> "Vector2":
        return Vector2(self.x * factor, self.y * factor)

    def __idiv__(self, factor: float) -> "Vector2":
        return Vector2(self.x / factor, self.y / factor)

    def mul(self, other: "Vector2") -> "Vector2":
        return Vector2(self.x * other.x, self.y * other.y)

    def dot(self, other: "Vector2") -> float:
        return self.x * other.x + self.y * other.y

    def length_squared(self) -> float:
        return self.dot(self)

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def unit(self) -> "Vector2":
        return self / self.length()

    def __repr__(self) -> str:
        return f"<{self.x}, {self.y}>"
