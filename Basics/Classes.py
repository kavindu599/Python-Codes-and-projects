# we use classes to define new types
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("draw")

# create objects

point1 = Point()
point1.x = 10
point1.y = 20

print(point1.x)
print(point1.y)

point2 = Point()
point2.x = 32
print(point2.x)