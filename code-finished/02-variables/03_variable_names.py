# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Naming Variables in Python
#
# Description:
# This script demonstrates the correct way to name variables in Python.
# It covers variable naming conventions, rules for valid and invalid
# variable names, and best practices.
# =======================================================================


def main():
    """
    Main function demonstrating how to name variables in Python.

    This function showcases how to create descriptive and valid variable names,
    following Python's naming rules and best practices. It also covers invalid
    variable names (commented out to avoid execution errors).
    
    No arguments or return values.
    """
    
    # Valid variable names
    user_name = "Alice"  # Using snake_case (common convention for variable names)
    user_age = 25  # Descriptive variable name
    total_price = 199.99  # Another descriptive name indicating what the value represents
    
    print(f"{user_name} is {user_age} years old.")
    
    # Best practices: Descriptive variable names
    temperature_in_celsius = 36.6  # Using descriptive names to indicate what the value represents
    print(f"The current temperature is {temperature_in_celsius}°C.")

    # Avoid using single-letter names unless in very simple contexts (e.g., in loops)
    for i in range(5):
        print(f"Loop iteration: {i}")

    # Avoid overwriting Python built-in functions
    # Avoid this:
    # list = [1, 2, 3]  # 'list' is a built-in function. Overwriting it can cause issues.

    # Use this instead:
    user_list = [1, 2, 3]  # Clear and does not overwrite the built-in 'list' function
    print(f"User list: {user_list}")

    # Python is case-sensitive: 'age' and 'Age' are different variables
    age = 30
    Age = 40
    print(f"age: {age}, Age: {Age}")

    # Variables with single-underscore or double-underscore prefixes (used for internal/private)
    _private_variable = "Private data"
    print(f"This is a private variable: {_private_variable}")

    # Variables with double underscore prefixes, typically used in classes for name mangling
    __internal_data = "Internal data for class use"
    print(f"This is an internal variable: {__internal_data}")

    # -----------------------------------
    # Non-valid variable names (commented out to avoid errors)
    # -----------------------------------
    # 2nd_user = "Bob"  # Invalid: Variable names cannot start with a number
    # user-name = "Bob"  # Invalid: Hyphens are not allowed in variable names
    # class = "Python"  # Invalid: 'class' is a reserved keyword
    # total price = 100  # Invalid: Spaces are not allowed in variable names

    # Correcting the above invalid names
    second_user = "Bob"  # Correct variable name (starts with a letter)
    user_name_alternative = "Bob"  # Using an underscore instead of a hyphen
    python_class = "Python 101"  # Avoid using reserved keywords like 'class'
    total_price_corrected = 100  # No spaces allowed, so we use underscores

    print(f"Second user is {second_user} and is taking the {python_class} course.")


# This is the standard boilerplate to call the main() function.
# It ensures that the script runs when executed directly.
if __name__ == "__main__":
    main()

# =======================================================================
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
