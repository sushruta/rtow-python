import dataclasses
import math


@dataclasses.dataclass()
class Vector3:
    x: float
    y: float
    z: float

    def __add__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self) -> "Vector3":
        return Vector3(-self.x, -self.y, -self.z)

    def mul(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __mul__(self, factor: float) -> "Vector3":
        return Vector3(self.x * factor, self.y * factor, self.z * factor)

    def __rmul__(self, factor: float) -> "Vector3":
        return self * factor

    def __truediv__(self, factor: float) -> "Vector3":
        return Vector3(self.x / factor, self.y / factor, self.z / factor)

    def __pos__(self) -> "Vector3":
        return self

    def __sub__(self, other: "Vector3") -> "Vector3":
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iadd__(self, other: "Vector3") -> "Vector3":
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other: "Vector3") -> "Vector3":
        return self.__iadd__(-other)

    def __imul__(self, factor: float) -> "Vector3":
        return self * factor

    def __idiv__(self, factor: float) -> "Vector3":
        return Vector3(self.x / factor, self.y / factor, self.z / factor)

    def dot(self, other: "Vector3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(u, v: "Vector3") -> "Vector3":
        return Vector3(u.y * v.z - u.z * v.y, u.z * v.x - u.x * v.z, u.x * v.y - u.y * v.x)

    def length_squared(self) -> float:
        return self.dot(self)

    def length(self) -> float:
        return math.sqrt(self.length_squared())

    def unit(self) -> "Vector3":
        return self / self.length()

    def __str__(self) -> str:
        return f"<{self.x}, {self.y}, {self.z}>"

    @property
    def r(self):
        return self.x

    @property
    def g(self):
        return self.y

    @property
    def b(self):
        return self.z
