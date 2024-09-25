# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Comments in Python
#
# Description:
# -----------
#   This script provides an overview of how to use different types of comments in
#   Python, including single-line comments, multi-line comments, and docstrings.
#
# © Copyright: Dr. Saad Laouadi
# =======================================================================

# 1. Single-line Comments:
# ------------------------
# * In Python, a single-line comment starts with the '#' symbol.
# * They are useful for adding short explanations or notes within your code.

# Example of a single-line comment:
print("Hello, World!")  # This prints a greeting message to the console

# Single-line comments can also be used to explain variables:
x = 10  # Assign the value 10 to the variable x

# 2. Multi-line Comments:
# -----------------------
# * Python does not have a native multi-line comment syntax like some other languages.
# * However, we can use triple-quoted strings (""" or ''') to achieve the same effect.

"""
This is an example of a multi-line comment in Python.
It spans across multiple lines.
Multi-line comments are often used for longer explanations
or temporarily disabling code blocks.
"""


# Another common approach is to use multiple single-line comments:
# This is a multi-line comment created by stacking
# single-line comments on top of each other.
# It's an alternative to using triple-quoted strings.


# 3. Documentation Strings (Docstrings):
# --------------------------------------
# Python uses docstrings (documentation strings) to document functions,
# classes, and methods. Docstrings are written using triple quotes (""" or ''')
# and are stored as part of the object's documentation.

# Docstrings can be accessed programmatically using functions like help() or
# by accessing the __doc__ attribute of a function or class.

# Example function with a docstring:
def square(x):
	"""
	This function calculates the square of a number.

	Args:
	- x (int or float): A numeric value to be squared.

	Returns:
	- int or float: The square of the input value.
	
	Example:
		>>> square(4)
	16

	This docstring can be accessed with help(square) or square.__doc__.
	"""
	return x ** 2


# Call the function with an example value:
result = square(4)
print(result)  # This should print 16

# 4. Inline Comments:
# -------------------
# Inline comments are single-line comments that appear on the same line as a statement.

y = 2 * 3  # Multiply 2 by 3 and assign the result to the variable y
print(y)  # This should print 6

# Additional Notes:
# -----------------
# - Single-line comments should be used sparingly and only when necessary to clarify the code.
# - Multi-line comments or docstrings are great for documenting larger code blocks or explaining
#   the purpose and usage of functions and classes.
# - Python encourages writing readable code that is self-explanatory, so aim to make your code
#   as clear as possible without overusing comments.
