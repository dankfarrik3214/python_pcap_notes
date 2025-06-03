"""
PCAP-31-03 Section 5.5 – Perform Input/Output Operations

Concepts Covered:
- open() function
- errno variable and values
- functions: close(), read(), write(), readline(), readlines()
- bytearray as input/output buffer
"""

import errno

# == The open() function ==
print("== Using open() ==")
try:
    file = open('sample.txt', 'w')  # Open for writing
    file.write("Line 1\nLine 2\nLine 3\n")
    file.close()
except OSError as e:
    if e.errno == errno.ENOENT:
        print("Error: File not found")
    else:
        print(f"OS error({e.errno}): {e.strerror}")


# == Reading from a file ==
print("\n== Reading with read() ==")
with open('sample.txt', 'r') as file:
    content = file.read()  # Read entire file
    print("Content from read():")
    print(content)


print("\n== Reading with readline() ==")
with open('sample.txt', 'r') as file:
    line = file.readline()  # Read single line
    prin
