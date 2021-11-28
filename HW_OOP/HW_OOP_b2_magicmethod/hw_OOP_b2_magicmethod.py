class Fraction:
    def __init__(self, nr, dr=1):
        if dr == 0:
            raise ZeroDivisionError("Mẫu số phải khác 0")

        if dr < 0:
            self.nr = nr * -1
            self.dr = dr * -1
        else:
            self.nr = nr
            self.dr = dr

        self._reduce()

    def __repr__(self):
        return "0" if self.nr == 0 else str(self.nr) if self.dr == 1 else f"{self.nr}/{self.dr}"

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) + (other.nr * self.dr), self.dr * other.dr)

    def __sub__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction((self.nr * other.dr) - (other.nr * self.dr), self.dr * other.dr)

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.nr, self.dr * other.dr)

    def __truediv__(self, other):
        if type(other) == int or type(other) == float:
            other = Fraction(other * self.dr, self.dr)

        return Fraction(self.nr * other.dr, other.nr * self.dr)

    def _reduce(self):
        n = hcf(self.nr, self.dr)

        if n:
            self.nr = int(self.nr / n)
            self.dr = int(self.dr / n)

def hcf(x, y):
    x, y = abs(x), abs(y)
    hcf = x if x < y else y

    while hcf > 0:
        if x % hcf == 0 and y % hcf == 0:
            break

        hcf -= 1

    return hcf if hcf > 0 else None

fr1 = Fraction(1, 2)
fr2 = Fraction(1.5, -3)

print("Phép tính với 2 Fraction:",fr1,"và",fr2)

print("Cộng:", fr1 + fr2)
print("Trừ: ",fr1 - fr2)
print("Nhân: ",fr1 * fr2)
print("Chia: ",fr1 / fr2)

fr = Fraction(1, 2)
print("Phép tính với 1 Fraction:", fr)

print("Cộng: ",fr + 1)
print("Trừ: ",fr - 1.5)
print("Nhân: ",fr * 2)
print("Chia: ",fr / 2)

