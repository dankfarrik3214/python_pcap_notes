"""
Now that you understand inheritance, it's time to examine one more property required for PCAP: __bases__. 
The __bases__ property of a class returns a tuple with all the base classes that the given class inherits from. 
"""

class Vehicle():
   pass
        
class Rideable():
   pass
      
class PetrolVehicle(Vehicle):
   pass
        
class Car(PetrolVehicle, Rideable):
   pass


# bases for Vehicle and Rideable
print(Vehicle.__bases__)
print(Rideable.__bases__)
# These two classes have no base classes defined within their brackets. 
# However, you will see __bases__ return (<class 'object'>,) for them. 
# The reason why these classes inherit automatically from object is mostly historical. 
# You do not need to worry about it in any way -- just keep in mind you will see object returned by __bases__ in such cases.



# bases for PetorlVehicle
print(PetrolVehicle.__bases__)
# This will return (<class '__main__.Vehicle'>,), as Vehicle is the only direct parent class for PetrolVehicle.



# bases for Car
print(Car.__bases__)
# This will return (<class '__main__.PetrolVehicle'>, <class '__main__.Rideable'>), 
# as Car has two direct parent classes: PetrolVehicle and Rideable. 
# We cannot see Vehicle here because Car inherits from it indirectly through PetrolVehicle.