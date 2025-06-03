"""
PCAP-31-03 Section 3.3 – Employ Built-in String Methods

Methods:
- .isxxx()
- .join()
- .split()
- .sort() (on lists)
- sorted()
- .index()
- .find()
- .rfind()
"""

# .isxxx() methods
# - Used to test string characteristics
# - Examples: isalpha(), isdigit(), islower(), isupper(), isspace()
print("\n.isxxx() examples:")
print("'Hello'.isalpha() =", 'Hello'.isalpha())  # True
print("'1234'.isdigit() =", '1234'.isdigit())    # True
print("'abc123'.isalnum() =", 'abc123'.isalnum())  # True

# .join()
# - Joins elements of an iterable into a single string
print("\n.join() example:")
words = ['Python', 'is', 'fun']
joined = ' '.join(words)
print("' '.join(['Python', 'is', 'fun']) =", joined)  # 'Python is fun'

# .split()
# - Splits a string into a list based on a delimiter
print("\n.split() example:")
sentence = "Python,is,awesome"
split_words = sentence.split(',')
print("'Python,is,awesome'.split(',') =", split_words)  # ['Python', 'is', 'awesome']

# .sort() vs sorted()
print("\n.sort() vs sorted() example:")
fruits = ['banana', 'apple', 'cherry']
# - .sort(): sorts a list in place
sorted_fruits = sorted(fruits)
print("sorted(fruits) =", sorted_fruits)  # ['apple', 'banana', 'cherry']
# - sorted(): returns a new sorted list
fruits.sort()
print("fruits after .sort() =", fruits)   # ['apple', 'banana', 'cherry']

# .index()
# - Returns the index of the first occurrence of a substring
print("\n.index() example:")
text = "banana"
print("text.index('a') =", text.index('a'))  # 1

# .find() and .rfind()
# - .find(): returns first index of substring, or -1 if not found
# - .rfind(): returns last index of substring, or -1 if not found
print("\n.find() and .rfind() examples:")
text = "banana"
print("text.find('a') =", text.find('a'))    # 1
print("text.rfind('a') =", text.rfind('a'))  # 5

# Summary:
# - .isxxx(): check string characteristics
# - .join(): combine strings with delimiter
# - .split(): break string into list
# - .sort(): sort list in-place
# - sorted(): return new sorted list
# - .index(): find position of substring (raises error if not found)
# - .find(), .rfind(): find substring (returns -1 if not found)
