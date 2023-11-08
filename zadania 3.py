# Task 1: Greeting function
def greet(name, surname):
    return f"Cześć {name} {surname}!"

# Task 2: Multiplication function
def multiply(x, y):
    return x * y

# Task 3: Check if number is even
def is_even(number):
    return number % 2 == 0

# Task 4: Check if the sum of the first two numbers is greater or equal to the third
def sum_greater_equal(x, y, z):
    return (x + y) >= z

# Task 5: Check if a list contains a specific value
def contains_value(lst, value):
    return value in lst

# Task 6: Merge lists, remove duplicates, and cube each element
def merge_and_cube(list1, list2):
    merged_list = list(set(list1 + list2))
    cubed_list = [x**3 for x in merged_list]
    return cubed_list