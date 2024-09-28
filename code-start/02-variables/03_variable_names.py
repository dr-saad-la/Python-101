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
    
    
    # Best practices: Descriptive variable names

    # Avoid using single-letter names unless in very simple contexts (e.g., in loops)

    # Avoid overwriting Python built-in functions
    # Avoid this:
    # list = [1, 2, 3]  # 'list' is a built-in function. Overwriting it can cause issues.

    # Use this instead:

    # Python is case-sensitive: 'age' and 'Age' are different variables

    # Variables with single-underscore or double-underscore prefixes (used for internal/private)

    # Variables with double underscore prefixes, typically used in classes for name mangling

    # -----------------------------------
    # Non-valid variable names (commented out to avoid errors)
    # -----------------------------------
    # 2nd_user = "Bob"  # Invalid: Variable names cannot start with a number
    # user-name = "Bob"  # Invalid: Hyphens are not allowed in variable names
    # class = "Python"  # Invalid: 'class' is a reserved keyword
    # total price = 100  # Invalid: Spaces are not allowed in variable names


if __name__ == "__main__":
    main()

# =======================================================================
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
