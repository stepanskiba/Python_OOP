class TriangleChecker:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def is_triangle(self):
        print(isinstance(self.a, int))
        if isinstance(self.a, int) or isinstance(self.a, float) and isinstance(self.b, int) or isinstance(self.b, float) and isinstance(self.c, int) or isinstance(self.c, float):
            if self.a >= 0 and self.b >= 0 and self.c >= 0:
                if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
                    return 3
                return 2
            return 1
        return 1

a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(TriangleChecker.is_triangle(tr))

