# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Constants in Python
#
# Description:
# This script introduces constants in Python, explaining the convention
# for naming them, and how they differ from variables. Constants are 
# values that are meant to remain unchanged throughout the program.
# =======================================================================


def main():
    """
    Main function demonstrating the use of constants in Python.

    Constants are generally written in all uppercase letters, and though Python
    does not have built-in support for constants (unlike other languages), 
    using naming conventions helps signal that certain values should not change.
    
    This function provides examples of defining constants, using them in
    calculations, and explaining best practices.
    
    No arguments or return values.
    """
    # Defining constants: Using uppercase letters and underscores
    PI = 3.14159  # Approximate value of Pi, used in circle calculations
    SPEED_OF_LIGHT = 299792458  # Speed of light in meters per second
    GRAVITY = 9.81  # Earth's gravity in meters per second squared

    # Demonstrating constant usage
    radius = 10  # Radius of a circle
    circumference = 2 * PI * radius  # Using the PI constant to calculate circumference
    print(f"The circumference of a circle with radius {radius} is {circumference:.2f} meters.")

    # Using constants in a physics calculation (falling object)
    mass = 70  # Mass of an object in kilograms
    weight = mass * GRAVITY  # Weight is mass * gravity
    print(f"An object with mass {mass}kg has a weight of {weight:.2f} newtons on Earth.")

    # Demonstrating a constant that should not change
    BIRTH_YEAR = 1995  # A birth year should remain constant throughout the program
    print(f"The birth year is set to: {BIRTH_YEAR}")

    # Best Practice: Even though constants can technically be modified, avoid doing so
    # unless absolutely necessary. For example, the following is allowed but not recommended:
    # PI = 3  # This is technically allowed, but it goes against the idea of constants
    # print(f"Modified PI value: {PI}")

    # However, modifying constants may lead to confusion, so always use constants carefully.
    # A better approach is to avoid reassigning or modifying constants once they are set.

    # Using a constant in a function call
    circle_area = calculate_circle_area(radius, PI)
    print(f"The area of a circle with radius {radius} is {circle_area:.2f} square meters.")


def calculate_circle_area(radius, pi_value):
    """
    Function to calculate the area of a circle.

    Parameters:
    - radius (float): The radius of the circle.
    - pi_value (float): The value of Pi (a constant).

    Returns:
    - float: The area of the circle.
    """
    return pi_value * (radius ** 2)


# This is the standard boilerplate to call the main() function.
# It ensures that the script runs when executed directly.
if __name__ == "__main__":
    main()

# =======================================================================
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================
