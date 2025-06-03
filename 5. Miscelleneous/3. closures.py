"""
PCAP-31-03 Section 5.3 – Define and Use Closures

Concepts Covered:
- Meaning and rationale for closures
- Defining and using closures
"""

# == Closure Example ==
print("== Basic Closure ==")

def make_multiplier(factor):
    # This is the closure
    def multiplier(number):
        return number * factor  # 'factor' is remembered
    return multiplier

times3 = make_multiplier(3)
times5 = make_multiplier(5)

print("3 * 10 =", times3(10))  # 30
print("5 * 10 =", times5(10))  # 50


# == What is a Closure? ==
# A closure is a function (multiplier) that 'remembers' variables (factor) from its enclosing scope,
# even if the enclosing function (make_multiplier) has finished execution.

print("\n== Closures Save State ==")

def greeting_maker(prefix):
    def greet(name):
        return f"{prefix}, {name}!"
    return greet

hello_greeter = greeting_maker("Hello")
bye_greeter = greeting_maker("Goodbye")

print(hello_greeter("Alice"))   # Hello, Alice!
print(bye_greeter("Bob"))       # Goodbye, Bob


# == Closure Properties ==
print("\n== Inspect Closure Properties ==")
print("Closure of times3:", times3.__closure__)
print("Captured value (factor) in times3:", times3.__closure__[0].cell_contents)
