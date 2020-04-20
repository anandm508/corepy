# Retreving last element using negative indexes

l = [1, 11, 111, 1111, 11111, 111111]

# Last element
l[-1]

# Second last element
l[-2]

# Slicing
# Extended form of indexing for referring to a portion of a list or other sequence
#Syntax: a_list[start:stop]

l[1:3]

# Take all elements except the first and the last
l[1:-1]

# Slice the list from the thirs ti the last
l[2:]

# Slice the list from the beginning upto the 2nd element but not including it
l[:2]

# Since both the start and stop are optional, it is even possible to pass them as empty and then get thge entire list back
l[:]

# Creating a new list object
c = l[:]

c is l  # Gives false as both the list are different objects
c == l  # Since the contents are same, gives True

# Other ways of coping list, they do only shallow copying
c = l.copy()
c is l  # Shorthand of id(c) == id(l)
c = list(l)
c is l  # Shorthand of id(c) == id(l)

# Proof of shallow copy, lets create a nested list
n = [[1, 2], [3.4]]
n_copy = n[:]
n_copy is n  # Returns false, parent list are different
n[0] is n_copy[0]  # Returns true, still child are same

# Add an item in the child, will get reflected in original as well as the copy
n[0].append(5)

# Both will have 5
n
n_copy

# For deeper copy refer copy module in the python standard library

# List multiplication
c = [21, 37]
d = c * 4
d
# Initilaizing a list of 0 withg length 9
l = [0] * 9
l
# Repetation works by coping the reference, lets see an example with a nested list
l = [[-1, 1]] * 5
# Now add something at 0 position list
l[0].append(9)
# The resultant list will have 9 in all the nested list
l

# Index
w = "the quick brown fox jumps over the lazy dog".split()
w
i = w.index("fox")
i
i = w.index("unicorn")
c = w.count("the")

# Test for membership using in/not in
37 in [1, 79, 9, 37, 345]
39 in [1, 79, 9, 37, 345]

# Removing a item from the list using the del keyword
u = "jackdaws loves my big sphinx of quartz".split()
u
# Remove using index
del u[3]
# Remove using value
u.remove('jackdaws')
# or try this one
del u[u.index('quartz')]
# Raises error when matching element is not present
u.remove('quartz')

# Inserting in a list
a = 'I accidentally the whole universe'.split()
a
# Insert the missing word
a.insert(2, "destroyed")
# Construct back to string format
' '.join(a)

# Adding lists
m = [2, 1, 3]
n = [4, 7, 11]
#Using + operator
k = m + n
k
# Using agumented operator
k += [18, 29, 47]
k
# Using extend operator
k.extend([76, 199, 299])
k


# List reverse
k.reverse()


# Sort the list
k.sort()

# Sort in reverse order
k.sort(reverse=True)
# Sort using a key
h = 'not perplexing do handwriting family where I illegebally know doctors'.split()
h
h.sort(key=len)
' '.join(h)


# Revering and sorting with affecting the origincal one
# Created a new revered list, without altering the original one
k_new = reversed(k)
list(k_new)
# Created a new sorted list, without altering the original one
k_new = sorted(k)
