import dataclasses
import math


@dataclasses.dataclass()
class Vector4:
    x: float
    y: float
    z: float
    w: float

    def __add__(self, other: "Vector4") -> "Vector4":
        return Vector4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __neg__(self) -> "Vector4":
        return Vector4(-self.x, -self.y, -self.z, -self.w)

    def mul(self, other: "Vector4") -> "Vector4":
        return Vector4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

    def __mul__(self, factor: float) -> "Vector4":
        return Vector4(self.x * factor, self.y * factor, self.z * factor, self.w * factor)

    def __rmul__(self, factor: float) -> "Vector4":
        return self * factor

    def __truediv__(self, factor: float) -> "Vector4":
        return Vector4(self.x / factor, self.y / factor, self.z / factor, self.w / factor)

    def __pos__(self) -> "Vector4":
        return self

    def __sub__(self, other: "Vector4") -> "Vector4":
        return Vector4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __iadd__(self, other: "Vector4") -> "Vector4":
        self.x += other.x
        self.y += other.y
        self.z += other.z
        self.w += other.w
        return self

    def __isub__(self, other: "Vector4") -> "Vector4":
        return self.__iadd__(-other)

    def __imul__(self, factor: float) -> "Vector4":
        return self * factor

    def __idiv__(self, factor: float) -> "Vector4":
        return Vector4(self.x / factor, self.y / factor, self.z / factor, self.w / factor)

    def dot(self, other: "Vector4") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def length_squared(self) -> float:
        return self.dot(self)

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def unit(self) -> "Vector4":
        return self / self.length()

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}, {self.z}, {self.w}>"

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z

    @property
    def a(self):
        return self.w
