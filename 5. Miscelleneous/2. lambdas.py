"""
PCAP-31-03 Section 5.2 – Embed Lambda Functions into the Code

Concepts Covered:
- Defining and using lambda functions
- Passing lambdas to other functions
- Built-in functions: map(), filter()
"""

# == Lambda Basics ==
print("== Basic Lambda ==")
square = lambda x: x ** 2
print("Square of 5:", square(5))  # 25


# == Lambdas passed to custom function ==
print("\n== Lambda Passed to Function ==")
def apply(func, value):
    return func(value)

result = apply(lambda x: x + 10, 7)
print("Result of apply(lambda x: x + 10, 7):", result)  # 17


# == Using map() with lambda ==
print("\n== map() with Lambda ==")
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print("Doubled:", doubled)  # [2, 4, 6, 8, 10]


# == Using filter() with lambda ==
print("\n== filter() with Lambda ==")
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", evens)  # [2, 4]


# == More readable alternative using def ==
print("\n== Named Function Alternative ==")
def is_even(n):
    return n % 2 == 0

filtered = list(filter(is_even, nums))
print("Even numbers using def:", filtered)
