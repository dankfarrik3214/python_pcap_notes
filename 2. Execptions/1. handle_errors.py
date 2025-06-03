"""
PCAP-31-03 Section 2.1 – Handle errors using Python-defined exceptions

Concepts Covered:
- except, except:, except: else:, except (e1, e2)
- the hierarchy of exceptions
- raise, raise ex
- assert
- except E as e
- the args property
"""

print("== Basic try/except ==")
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Caught division by zero!")


print("\n== except without specifying error (catch-all) ==")
try:
    x = int("not a number")
except:
    print("Caught a general exception")


print("\n== except with else block ==")
try:
    x = 10
    y = 5
    result = x / y
except ZeroDivisionError:
    print("Division failed.")
else:
    print("Division succeeded. Result:", result)


print("\n== except with multiple exception types ==")
try:
    # Try uncommenting one at a time to test
    # value = int("abc")
    value = [][0]
except (ValueError, IndexError):
    print("Caught either ValueError or IndexError")


print("\n== Exception hierarchy demonstration ==")
try:
    x = int("abc")
except Exception:
    print("Caught something in the Exception hierarchy")


print("\n== raise and raise ex ==")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")

try:
    check_age(-1)
except ValueError as e:
    print("Raised manually:", e)


print("\n== assert statement ==")
def calculate_discount(price):
    assert price >= 0, "Price can't be negative"
    return price * 0.9

try:
    calculate_discount(-10)
except AssertionError as e:
    print("Assertion triggered:", e)


print("\n== except E as e and e.args ==")
try:
    raise RuntimeError("Something bad happened", 42)
except RuntimeError as e:
    print("Caught:", e)
    print("Type:", type(e))
    print("Args:", e.args)
    print("Message:", e.args[0])
    print("Code:", e.args[1])
