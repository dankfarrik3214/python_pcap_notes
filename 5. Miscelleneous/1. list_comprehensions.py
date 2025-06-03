"""
PCAP-31-03 Section 5.1 – Build Complex Lists Using List Comprehension

Concepts Covered:
- list comprehensions
- the if operator
- nested comprehensions
"""

# == Basic list comprehension ==
print("== Basic List Comprehension ==")
squares = [x**2 for x in range(5)]
print("Squares:", squares)  # [0, 1, 4, 9, 16]


# == List comprehension with if filter ==
print("\n== List Comprehension with If Filter ==")
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)  # [0, 2, 4, 6, 8]


# == List comprehension with if-else expression ==
print("\n== List Comprehension with If-Else Expression ==")
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print("Labels:", labels)  # ['even', 'odd', 'even', 'odd', 'even']


# == Nested list comprehension ==
print("\n== Nested List Comprehension (2D grid) ==")
matrix = [[row * col for col in range(3)] for row in range(3)]
print("Matrix:")
for row in matrix:
    print(row)
# Output:
# [0, 0, 0]
# [0, 1, 2]
# [0, 2, 4]

# Flatten a 2D list
print("\n== Flattened Matrix ==")
flattened = [cell for row in matrix for cell in row]
print("Flattened:", flattened)  # [0, 0, 0, 0, 1, 2, 0, 2, 4]
