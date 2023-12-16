# Task 1: 
def greet(name, surname):
    return f"Cześć {name} {surname}!"

# Task 2: 
def multiply(x, y):
    return x * y

# Task 3: 
def is_even(number):
    return number % 2 == 0

# Task 4: 
def sum_greater_equal(x, y, z):
    return (x + y) >= z

# Task 5: 
def contains_value(lst, value):
    return value in lst

# Task 6: 
def merge_and_cube(list1, list2):
    merged_list = list(set(list1 + list2))
    cubed_list = [x**3 for x in merged_list]
    return cubed_list
