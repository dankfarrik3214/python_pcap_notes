"""
PCAP-31-03 Section 2.2 – Extend the Python Exceptions Hierarchy with Self-Defined Exceptions

Concepts Covered:
- self-defined exceptions
- defining and using self-defined exceptions
"""

# == Step 1: Define a custom exception ==
class TooSmallError(Exception):
    """Raised when a value is too small."""
    def __init__(self, value, message="Value is too small"):
        self.value = value
        self.message = message
        super().__init__(self.value, self.message)

# == Step 2: Use the custom exception ==
def check_value(x):
    if x < 10:
        raise TooSmallError(x)

print("== Custom Exception Usage ==")
try:
    check_value(5)
except TooSmallError as e:
    print("Caught custom exception!")
    print("Type:", type(e))
    print("Args:", e.args)
    print(f"Message: {e.message} | Value: {e.value}")

# == Step 3: Show that it's part of the exception hierarchy ==
print("\n== isinstance checks ==")
print("Is TooSmallError a subclass of Exception?", issubclass(TooSmallError, Exception))
print("Is TooSmallError a subclass of BaseException?", issubclass(TooSmallError, BaseException))
