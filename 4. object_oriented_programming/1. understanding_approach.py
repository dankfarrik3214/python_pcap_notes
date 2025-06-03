"""
PCAP-31-03 Section 4.1 – Understand the Object-Oriented Approach

Concepts Covered:
- class, object
- property (attributes)
- method (functions inside classes)
- encapsulation
- inheritance
- superclass, subclass
- identifying class components


Key Notes:
- A class should always have a constructor (__init__) to initialize attributes.
- Attributes are variables that store object state and are defined in the constructor or class body.
- Methods are functions defined inside a class and operate on object data using 'self'.
- The 'self' keyword refers to the current object instance.
- Encapsulation is implemented by using private attributes (prefix with '__') and exposing them via methods.
- A subclass inherits from a superclass and can override or extend its behavior.
- Use `super().__init__()` in a subclass to call the constructor of the superclass.
- Classes act as blueprints; objects are instances created from those blueprints.
"""

# Class definition
class Animal:
    """
    Superclass: Animal
    Demonstrates basic properties, methods, and encapsulation
    """
    def __init__(self, name):
        self.name = name  # property (attribute)

    def speak(self):  # method
        return f"{self.name} makes a sound"

# Object creation
animal = Animal("GenericAnimal")
print("Object example:")
print(animal.name)         # Access property
print(animal.speak())      # Call method

# Subclass with inheritance
class Dog(Animal):
    """
    Subclass: Dog
    Inherits from Animal and overrides the speak() method
    """
    def speak(self):  # method overriding
        return f"{self.name} says Woof!"

dog = Dog("Rex")
print("\nInheritance and Method Overriding:")
print(dog.name)           # Inherited property
print(dog.speak())        # Overridden method

# Encapsulation example with private variable
class Secret:
    def __init__(self):
        self.public_info = "Visible"
        self.__private_info = "Hidden"  # double underscore makes it private

    def reveal_secret(self):
        return self.__private_info

secret = Secret()
print("\nEncapsulation example:")
print("Public:", secret.public_info)
# print("Private:", secret.__private_info)  # Would raise AttributeError
print("Accessed via method:", secret.reveal_secret())

# Summary:
# - A class defines a blueprint, objects are instances of that class
# - Properties store data (attributes), methods define behavior
# - Inheritance allows reuse and extension of behavior
# - Encapsulation hides internal state using access control
# - Subclasses inherit from superclasses and can override methods
