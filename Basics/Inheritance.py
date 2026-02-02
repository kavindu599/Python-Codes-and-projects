class Mamal:
    def walk(self):
        print("Walk")

class Dog(Mamal):
    def bark(self):
        print("Bark")
    

class Cat(Mamal):
    def annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()
dog1.bark()

print("\n")

cat1 = Cat()
cat1.walk()
cat1.annoying()


