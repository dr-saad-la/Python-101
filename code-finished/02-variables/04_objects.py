# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Objects in Python (id, memory address, and type)
#
# Description:
# This script introduces the concept of objects in Python. It covers
# how Python manages objects in memory, how to get the unique ID (memory
# address) of an object using the `id()` function, and how to check the
# data type of an object using the `type()` function.
# =======================================================================

def main():
    """
    Main function demonstrating the concept of objects in Python.

    This function covers how to inspect an object’s identity, type, and
    memory address using Python's built-in functions: `id()`, `type()`, and `is`.
    It also demonstrates how Python manages object references and memory usage.

    No arguments or return values.
    """

    # Example 1: Understanding objects and identity
    a = 10
    b = 10

    print(f"Value of a: {a}, Value of b: {b}")

    # Checking if the two variables point to the same object in memory
    print(f"Are a and b the same object? {a is b}")

    # Using id() to find the memory address (identity) of the object
    print(f"Memory address of a: {id(a)}")
    print(f"Memory address of b: {id(b)}")

    # Checking the type of the object
    print(f"Type of a: {type(a)}")
    print(f"Type of b: {type(b)}")

    # Example 2: Assigning new objects to variables
    a = a + 1  # This creates a new object and assigns it to 'a'
    print(f"New value of a: {a}")
    print(f"New memory address of a: {id(a)}")
    print(f"Memory address of b: {id(b)}")

    # Example 3: Objects with mutable types (lists)
    list1 = [1, 2, 3]
    list2 = list1  # Both list1 and list2 point to the same object

    print(f"list1: {list1}, list2: {list2}")
    print(f"Memory address of list1: {id(list1)}")
    print(f"Memory address of list2: {id(list2)}")

    # Modifying the list (mutating it)
    list1.append(4)
    print(f"After modification - list1: {list1}, list2: {list2}")
    print(f"Memory address of list1: {id(list1)} (Still the same)")

    # Example 4: Objects with immutable types (strings)
    s1 = "hello"
    s2 = s1
    print(f"s1: {s1}, s2: {s2}")
    print(f"Memory address of s1: {id(s1)}")
    print(f"Memory address of s2: {id(s2)}")

    s1 = s1 + " world"  # This creates a new string object
    print(f"After modification - s1: {s1}, s2: {s2}")
    print(f"New memory address of s1: {id(s1)}")
    print(f"Memory address of s2 (unchanged): {id(s2)}")

    # Example 5: Checking object identity and reference equality
    x = [1, 2, 3]
    y = [1, 2, 3]

    print(f"x == y: {x == y}")  # True because they contain the same values
    print(f"x is y: {x is y}")  # False because they are different objects in memory

def explain():
    """
    Explanation of key concepts:
    - `id()`: Returns the identity (memory address) of an object.
    - `type()`: Returns the data type of an object.
    - `is`: Checks whether two variables point to the same object in memory.

    Objects in Python can be mutable (like lists) or immutable (like integers or
    strings).
    Mutable objects can change their content without changing their identity.
    Immutable objects create a new object in memory when they are changed.
    """
    print("""
    - id(): Returns the memory address (unique identifier) of an object.
    - type(): Returns the data type of an object.
    - is: Checks if two variables refer to the same object in memory.

    Python manages memory efficiently, so sometimes multiple variables might
    point to the same object if they have the same immutable value.
    """)


# This is the standard boilerplate to call the main() function.
if __name__ == "__main__":
    main()
    explain()

# =======================================================================
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
