from point import Point


point = Point(12, 5)
print(point.get_x())
print(point.get_y())

point.set_x(42)
print(point.get_x())

print(point._x)
print(point._y)
