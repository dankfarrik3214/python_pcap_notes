"""
PCAP-31-03 Section 5.4 – Understand Basic Input/Output Terminology

Concepts Covered:
- I/O modes
- Predefined streams
- Handles vs. Streams
- Text vs. Binary modes
"""

import sys

# == I/O Modes ==
# 'r'  - read (default)
# 'w'  - write (truncates existing file)
# 'a'  - append
# 'rb' - read binary
# 'wb' - write binary

print("== I/O Modes ==")
# Open a file for writing text
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")

# Read the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File content:", content.strip())


# Write binary data
print("\n== Binary Mode ==")
with open('binary_example.bin', 'wb') as file:
    file.write(b'\x00\xFF\x10')  # Writing raw bytes

# Read binary data
with open('binary_example.bin', 'rb') as file:
    data = file.read()
    print("Binary content:", data)


# == Predefined Streams ==
print("\n== Predefined Streams ==")
print("This goes to stdout")
sys.stderr.write("This is an error message to stderr\n")

# Note: `sys.stdin` would require user input, for example:
# user_input = sys.stdin.readline()


# == Handles vs. Streams ==
print("\n== Handles vs. Streams ==")
# A *handle* is a reference to an open file (object returned by open())
# A *stream* is the actual flow of data (input/output)

# Example: 'file' here is a handle to the file stream
with open('example.txt', 'r') as handle:
    print("Handle name:", handle.name)
    print("Handle mode:", handle.mode)

# sys.stdout is a predefined output stream
print("sys.stdout is a stream object:", isinstance(sys.stdout, object))


# == Text vs. Bi
