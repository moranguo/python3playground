class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __str__(self):
        return "Point x is %s and y is %s" % (self.x, self.y)


if __name__ == "__main__":
    a = Point(1, 2)
    b = Point(1, 2)
    c = Point(3, 4)
    print(a == b)
    print(a == c)
    print(a)
    a + c
    print(a)
