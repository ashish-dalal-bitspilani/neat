# In Python, comprehensions provide a concise way to create collections like lists, dictionaries, sets,
# and even generators. Here’s a breakdown of the most common comprehensions:

# List comprehension  :
# Syntax : [expression for item in iterable if condition]
# Example :
squares = [x**2 for x in range(5)]
print(squares)

# Dictionary comprehension :
# Syntax : {key_expression : value_expression for item in iterable if condition}
# Example :
square_dict = {x: x**2 for x in range(5)}
print(square_dict)

# Set comprehension :
# {element_expression for item in iterable if condition}
# Example :
unique_squares = {x**2 for x in range(-5, 6)}
print(unique_squares)

# Generator Comprehension
# Returns a generator, which is an iterator that yields items one at a time rather than creating an entire list in memory
# Syntax : (expression for item in iterable if condition)
square_gen = (x**2 for x in range(5))
print(square_gen)
# Output: <generator object <genexpr> at 0x...>
# To view the items, you would typically iterate over the generator:
for num in square_gen:
    print(num)

tuple_comprehension = tuple(i for i in range(5))
print(tuple_comprehension)

generator_comprehension = (i for i in range(5))
print(generator_comprehension)