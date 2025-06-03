"""
PCAP-31-03 Section 4.3 – Equip a Class with Methods

Concepts Covered:
- Declaring and using methods
- The self parameter

Key Notes:
- Methods are functions defined inside a class.
- All instance methods must take 'self' as the first parameter.
- 'self' refers to the specific object calling the method.
- Methods can read or update the object's attributes using 'self'.
- Without 'self', the method would not know which object it belongs to.
"""

# Class with methods and self usage
class Calculator:
    def __init__(self, initial=0):
        self.value = initial  # Instance variable

    def add(self, amount):
        self.value += amount

    def subtract(self, amount):
        self.value -= amount

    def reset(self):
        self.value = 0

    def get_value(self):
        return self.value


# Using the class and its methods
calc = Calculator()
print("Initial value:", calc.get_value())  # 0

calc.add(10)
print("After adding 10:", calc.get_value())  # 10

calc.subtract(3)
print("After subtracting 3:", calc.get_value())  # 7

calc.reset()
print("After reset:", calc.get_value())  # 0

# Demonstrating 'self' with multiple instances
print("\nMultiple object demo:")

c1 = Calculator()
c2 = Calculator(50)

c1.add(5)
c2.subtract(10)

print("c1 value:", c1.get_value())  # 5
print("c2 value:", c2.get_value())  # 40

# Summary:
# - Methods are declared using 'def' inside a class.
# - The first argument of every instance method must be 'self'.
# - 'self' allows the method to access or modify the current object’s data.
# - Each object has its own data; methods operate on that data using 'self'.
