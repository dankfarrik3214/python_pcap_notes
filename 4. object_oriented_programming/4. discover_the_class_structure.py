"""
PCAP-31-03 Section 4.4 – Discover the Class Structure

Concepts Covered:
- Introspection
- hasattr() function (objects vs. classes)
- Special class properties: __name__, __module__, __bases__

Key Notes:
- Introspection allows examining the structure of objects and classes at runtime.
- The built-in `hasattr(obj, 'attr')` function checks if an object or class has a given attribute.
- `__name__` gives the class name.
- `__module__` tells which module the class is defined in.
- `__bases__` returns a tuple of the base classes (superclasses).
"""

# Sample base and derived classes
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        return f"{self.brand} {self.model} is driving."


# Introspection using hasattr
print("hasattr() function:")
car = Car("Toyota", "Corolla")

print("Does car have attribute 'brand'? ->", hasattr(car, 'brand'))  # True
print("Does car have method 'drive'? ->", hasattr(car, 'drive'))    # True
print("Does car have attribute 'wheels'? ->", hasattr(car, 'wheels'))  # False

print("\nClass vs Object hasattr:")
print("Does Car class have '__init__'? ->", hasattr(Car, '__init__'))  # True
print("Does Car class have 'model'? ->", hasattr(Car, 'model'))        # False

# __name__, __module__, __bases__
print("\nClass Structure Properties:")
print("Car.__name__ =", Car.__name__)         # 'Car'
print("Car.__module__ =", Car.__module__)     # Usually '__main__' if run directly
print("Car.__bases__ =", Car.__bases__)       # Tuple of base classes (e.g., (<class '__main__.Vehicle'>,))

# Summary:
# - hasattr() is useful to check if an attribute/method exists before accessing it.
# - __name__: shows the name of the class as a string.
# - __module__: shows the module name where the class was defined.
# - __bases__: shows the base class(es) used in inheritance.
# - Introspection helps in debugging and understanding object structures at runtime.
