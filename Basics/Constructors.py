class Point:

    # use constructors
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point = Point(10, 30)
point.x = 11
print(point.x)


# Excercise 2
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f"Hi I am {self.name}")

person1 = Person("John")
print(person1.name)
person1.talk()