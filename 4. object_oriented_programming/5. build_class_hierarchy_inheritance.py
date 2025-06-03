"""
PCAP-31-03 Section 4.5 – Build a class hierarchy using inheritance

Concepts Covered:
- single and multiple inheritance
- the isinstance() function
- overriding
- operators: not, is, is not
- polymorphism
- overriding the __str__() method
- diamonds
"""

# == Single Inheritance ==
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Single inheritance
    def speak(self):
        return "Woof!"  # Overriding

print("Single Inheritance and Overriding:")
d = Dog()
print(d.speak())  # Woof!
print(isinstance(d, Animal))  # True


# == Multiple Inheritance ==
class Walker:
    def move(self):
        return "Walking"

class Swimmer:
    def move(self):
        return "Swimming"

class Amphibian(Walker, Swimmer):  # Multiple inheritance
    pass

print("\nMultiple Inheritance (Method Resolution Order):")
a = Amphibian()
print(a.move())  # Walker.move is used first due to MRO
print(Amphibian.__mro__)  # Show method resolution order


# == Overriding __str__ and Polymorphism ==
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

class Employee(Person):
    def __str__(self):
        return f"Employee: {self.name}"

def print_identity(obj):
    print(str(obj))  # Polymorphism: calls correct __str__()

print("\nPolymorphism and __str__ Overriding:")
p = Person("Alice")
e = Employee("Bob")
print_identity(p)
print_identity(e)


# == Diamond Problem (Multiple inheritance with common base) ==
class A:
    def say(self):
        return "A"

class B(A):
    def say(self):
        return "B"

class C(A):
    def say(self):
        return "C"

class D(B, C):  # Diamond shape: D → B → A, D → C → A
    pass

print("\nDiamond Inheritance Example:")
d = D()
print(d.say())  # Output: B due to MRO
print(D.__mro__)  # See the method resolution order


# == 'is', 'is not', 'not' operators ==
print("\nIdentity and Logical Operators:")
x = [1, 2]
y = x
z = [1, 2]

print("x is y:", x is y)         # True (same object)
print("x is z:", x is z)         # False (different object with same value)
print("x is not z:", x is not z) # True
print("not False:", not False)  # True
