# =======================================================================
# Author: Dr. Saad Laouadi
# Course: Python-101
# Lesson: Variables in Python
#
# Description:
# This script introduces the concept of variables in Python. It covers how
# to define, assign, reassign, and manipulate variables. The script includes
# different data types such as strings, integers, booleans, lists, and dictionaries.
# It also shows how to use variables with functions and conditionals.
# =======================================================================


def main():
	"""
	Main function demonstrating the use of variables in Python.

	This function explores variable assignment, usage, reassignment,
	and printing values to the console. It covers string concatenation,
	numeric operations, lists, dictionaries, and basic conditionals,
	showing how variables are fundamental to storing and manipulating data.

	No arguments or return values.
	"""
	# String variables: Storing user details
	user_name = "Alice"
	greeting = "Hello"
	
	# Integer and float variables: Age and height
	user_age = 25
	user_height = 5.7  # Height in feet
	
	# Concatenate and print the string and variable values
	print(f"{greeting}, {user_name}! You are {user_age} years old and {user_height} feet tall.")
	
	# Reassigning variables: Simulating a birthday
	user_age += 1  # Incrementing the age by 1
	print(f"Next year, {user_name}, you will be {user_age} years old.")
	
	# Mathematical operations: Calculating the area of a rectangle
	width = 10
	height = 5
	area = width * height
	print(f"The area of a rectangle with width {width} and height {height} is {area} square units.")
	
	# Boolean variable: Checking if it's raining
	is_raining = True
	if is_raining:
		print("It's raining, better take an umbrella.")
	else:
		print("No need for an umbrella today.")
	
	# List variables: Storing and printing a list of favorite foods
	favorite_foods = ["Pizza", "Sushi", "Chocolate", "Ice Cream"]
	print(f"{user_name}'s favorite foods are: {favorite_foods}")
	
	# Adding a new food to the list
	favorite_foods.append("Pasta")
	print(f"Updated list of favorite foods: {favorite_foods}")
	
	# Dictionary variable: Storing information about a product
	product = {
			"name": "Laptop", "price": 999.99, "in_stock": True, "categories": ["Electronics", "Computers"]
			}
	print(f"Product Name: {product['name']}, Price: ${product['price']}")
	
	# Updating the dictionary
	product["price"] = 949.99  # Applying a discount
	print(f"Updated price after discount: ${product['price']}")
	
	# Calling a function that uses variables
	result = calculate_discount(product["price"], 10)
	print(f"Price after 10% discount: ${result:.2f}")
	
	# Using variables in a loop: Counting down from 5
	countdown = 5
	while countdown > 0:
		print(f"Countdown: {countdown}")
		countdown -= 1
	print("Blast off!")
	
	# Storing user input in a variable
	color = input("What's your favorite color? ")
	print(f"{user_name}'s favorite color is {color}.")


def calculate_discount(price, discount_percent):
	"""
	Function to calculate a discount on a given price.

	Parameters:
	- price (float): The original price of the product.
	- discount_percent (float): The discount percentage to apply.

	Returns:
	- float: The final price after applying the discount.
	"""
	discount_amount = price * (discount_percent / 100)
	final_price = price - discount_amount
	return final_price


# This is the standard boilerplate to call the main() function.
# It ensures that the script runs when executed directly.
if __name__ == "__main__":
	main()

# =======================================================================
# © Copyright: Dr. Saad Laouadi
# All Rights Reserved 🛡️
# =======================================================================