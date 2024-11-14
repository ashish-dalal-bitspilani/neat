# In Python, functions are mutable objects, meaning that their attributes or properties can be modified,
# but the function itself is generally treated as immutable in terms of its core behavior.

# Here's a breakdown of how functions work in terms of mutability:

# Functions in Python:

# Function objects themselves are mutable, meaning you can modify their attributes, such as the
# __doc__ (docstring), __name__, and other custom attributes you might assign to them.

# The function's behavior or code (the logic that the function performs) is immutable.
# You cannot change the body of a function once it has been defined. However, you can rebind or
# overwrite the function name itself.

# Examples:
# Modifying Function Attributes (Mutable):
# You can assign or change the attributes of a function.
def my_function():
    return "Hello"

# Modifying the docstring
my_function.__doc__ = "This is my modified function"

# Checking the new docstring
print(my_function.__doc__)  # Output: This is my modified function

# Rebinding a Function (Mutable):
# You can assign a new function to the same variable, effectively changing its behavior.
def my_function():
    return "Hello"

# Rebinding the function
def new_function():
    return "Goodbye"

my_function = new_function

print(my_function())  # Output: Goodbye

# Function Code (Immutable):
# You cannot directly modify the code or body of a function after it has been defined.
def my_function():
    return "Hello"

print(my_function())
print(my_function.__code__)
print(type(my_function.__code__))
my_function.__code__ = compile(source = "x = 10\nprint(x)", filename= "test", mode="exec")
my_function()
# This will raise an error:
# my_function.__code__ = new_code  # TypeError: 'function' object attribute 'code' is read-only