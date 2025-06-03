"""
PCAP-31-03 Section 4.6 – Construct and Initialize Objects

Concepts Covered:
- Declaring constructors
- Invoking constructors
"""

# == Declaring a constructor ==
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand            # Instance variable
        self.year = year              # Instance variable
        print(f"Vehicle constructed: {self.brand}, {self.year}")

# == Invoking the constructor ==
print("Constructing and initializing objects:")
v1 = Vehicle("Toyota", 2020)
v2 = Vehicle("Ford", 2023)

# Show object data
print(f"{v1.brand} was made in {v1.year}")
print(f"{v2.brand} was made in {v2.year}")

# Another example with optional/default constructor values
class Gadget:
    def __init__(self, name="Unknown", price=0):
        self.name = name
        self.price = price

print("\nDefault values in constructors:")
g1 = Gadget()
g2 = Gadget("Smartwatch", 199)

print(f"{g1.name} costs {g1.price}")
print(f"{g2.name} costs {g2.price}")