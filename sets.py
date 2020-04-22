"""
Unordered collection of unique elements

Sets are mutable

Elements in a set must be immutable

Sets are dilimited by curly braces {}

"""

p = {6, 6, 28, 496, 8128, 33553066}
# Result is unordered, duplicates will be discarded
p
type(p)

# Empty curly braces will result in a dictionary
d = {}
type(d)

# To create an empty set use the set constructor
e = set()
type(e)

# Set can also be created using the set constructor
# This example also shows how set can be used to remove duplicates from the list
s = set([6, 6, 28, 496, 8128, 33553066])
s

# Iterating over a list
for x in {6, 28, 496, 8128, 33553066}:
    print(x)

# Membership operators in and not in
6 in {6, 28, 496, 8128, 33553066}
9 not in {6, 28, 496, 8128, 33553066}

# Adding elements
k = {81, 108}
k
k.add(54)
k
# Adding an element which already exists has no effect
k.add(81)
k
k.update([37, 128, 97])
k
k.update({47, 54, 39})
k

# Removing elements
k.remove(97)
k
# Removing an element which does not exist in the list throws key error
k.remove(98)
# Use discard, to even remove elements which do not exist in the list.
# Discard does not throw key error
k.discard(98)

# Making copies
# Shallow copy is made
j = k.copy()
j
l = set(k)
l


# ****************************
# SET ALGEBRA
# union, difference, intersection,
# subset, superset, disjoint
# ****************************
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

# Returns all the value present in both the sets
blue_eyes.union(blond_hair)
# Union is a commutative operator
blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes)

# Returns all the names with both blue eyes and blond hairs
blue_eyes.intersection(blond_hair)
# intersection is a commutative operator
blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes)

# Returns all the names with blond hairs without blue eyes
blond_hair.difference(blue_eyes)
# difference is non commutative operator
blue_eyes.difference(blond_hair) == blond_hair.difference(blue_eyes)

# Symmetric Difference
# Either have blue eyes or blomd hairs but not both
blond_hair.symmetric_difference(blue_eyes)
# symmetric_difference is commutative operator
blue_eyes.symmetric_difference(
    blond_hair) == blond_hair.symmetric_difference(blue_eyes)


# Sub set
# All the people who can smell HCN have blond hairs
smell_hcn.issubset(blond_hair)

# Super set
# All the member of the second set are present in the first set
taste_ptc.issuperset(smell_hcn)

# Disjoint
# Both the sets are entirely different, with no common elements
a_blood.isdisjoint(b_blood)
