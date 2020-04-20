"""Demo of built in collections tuple, tuples are immutable
    tuples are Wrapped in ()
"""
t = ("Norway", 4.953, 3)  # Created a tuple

# Accessing the tuple elements
t[0]
t[1]
t[2]

# length of the tuple
len(t)

# Iteration
for item in t:
    print(item)

# Concatanating tuples using the  + operator
# Will create a new tuple
t + (338186.0, 265e9)

# Tuple multiplication
# Will append the items thrice but will return a new tuple
t * 3

# Nested tuples
a = ((208, 24564), (2545, 698960), (234348, 78987), ("sadasd", 54))

a[2][1]

# Single element tuple, note the comma at the end
h = (391,)

# Empty tuple
e = ()

# Tuple without brackets
p = 1, 1, 1, 4, 6, 19

type(p)


def minmax(items):
    """Create a function to create a min max tuple"""
    return min(items), max(items)


# With a tuple input
minmax((1, 2, 3, 4, 5, 6, 7, 8, 9))
# With a list input
minmax([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Wonderful feature of python
# TUPLE UNPACKING
lower, upper = minmax([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(lower)
print(upper)
# Works well with nested tuple as well
(a, (b, (c, d))) = (4, (3, (2, 1)))
a
b
c
d

# Swapping is so easy with tuple unpacking feature
a = "jelly"
b = "bean"
a, b = b, a
b
a
# Creating a tuple from an existing object
tuple([21, 65, 87, 654])
tuple("Karnataka")

# Using in and not in operator
5 in (3, 5, 17, 257, 65537)
5 not in (3, 5, 17, 257, 65537)
