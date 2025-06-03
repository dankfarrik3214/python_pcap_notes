"""
PCEP-31-03 Section 4.2 – Employ Class and Object Properties

Concepts Covered:
- instance vs. class variables: declarations and initializations
- the __dict__ property (objects vs. classes)
- private components (instances vs. classes)
- name mangling
"""

# == Example 1: Class, Instance, Local Variables ==
class Building:
  total_buildings = 0  # Class variable (shared)

  def __init__(self, location, size, value):
    self.location = location     # Instance variable (unique)
    self.size = size
    self.value = value
    Building.total_buildings += 1

    # Demonstrate scope of class, instance, and local variables
    Building.rating = "basic"     # Class variable
    self.rating = "standard"      # Instance variable
    rating = "luxury"             # Local variable

    print("Class variable:", Building.rating)
    print("Instance variable:", self.rating)
    print("Local variable:", rating)

  def describe(self):
    print(f"The building at {self.location} is {self.size} sqm and valued at {self.value}.")


b1 = Building("Main Street 101", 250, 900000)
b1.describe()
print("Total buildings:", Building.total_buildings)


# == Example 2: __dict__ properties ==
print("\n__dict__ of the instance:")
print(b1.__dict__)  # Instance variables only

print("\n__dict__ of the class:")
for key in Building.__dict__:
  print(" ", key)


# == Example 3: Counter class (instance vs. class variable clearly) ==
class Tracker:
  total_count = 0  # Class variable

  def __init__(self, label):
    self.label = label      # Instance variable
    self.count = 0

  def track(self):
    self.count += 1
    Tracker.total_count += 1


print("\nInstance vs. Class Variables (Tracker):")
t1 = Tracker("Sensor A")
t2 = Tracker("Sensor B")

t1.track()
t2.track()
t2.track()

print(f"{t1.label} count:", t1.count)  # 1
print(f"{t2.label} count:", t2.count)  # 2
print("Total tracked (class variable):", Tracker.total_count)

print("\n__dict__ of Tracker object:")
print(t1.__dict__)


# == Example 4: Private variable and name mangling ==
class Vault:
  def __init__(self):
    self.visible_item = "open"
    self.__hidden_item = "locked"  # Private variable

  def get_hidden(self):
    return self.__hidden_item


v = Vault()
print("\nName Mangling Demonstration:")
print("Public item:", v.visible_item)

# This would raise an error: print(v.__hidden_item)
print("Access via name mangling:", v._Vault__hidden_item)

print("\nSummary:")
print("Original private name: __hidden_item")
print("Mangled name:         _Vault__hidden_item")
