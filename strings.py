import datetime
import math
len("qwqertrtyfjgcfgdsrdtfhgjmbnvxdsadfgjnvcxdfsaergdhjmb")

"New" + "Found" + "Land"

s = "New"
s += "Found"
s += "land"

print(s)

# Strings are immutable
# Using the join operator. Preferred over + operator as it saves temporary space
colours = ";".join(["#45ff23", "#2321fa", "#1298a3", "#a32312"])
colours
colours.split(";")

# Using join on an empty string
"".join(["high", "way", "man"])

# Using partitioning, returns a tuple
"unforgetable".partition("forget")

departure, seperator, arrival = "Bangalore:Ranchi".partition(":")
departure
arrival
# _ is for unused or dummy values
origin, _, destination = "Seattle-Boston".partition("-")

# String formatting
"The age of {0} is {1}".format("Anand", 33)
"The age of {0} is {1}. {0}'s birthday is on {2}".format(
    "Anand", 33, "15th-DEC")
"Recalculating spline {} of {}".format(4, 23)
"Current position {latitude} and {longitude}".format(
    latitude="60N", longitude="5E")

"Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(
    pos=(65.2, 23.1, 82.2))
# Uses import math
"Math constants: pi={m.pi}, e={m.e}".format(m=math)

value = 4*20
"The value is {value}".format(value=value)

# PEP-498: Literal String Interpolation
f'The value is {value}'
f'The current time is {datetime.datetime.now().isoformat()}'
f'Math constants: pi={math.pi}, e={math.e}'
f'Math constants: pi={math.pi:.3f}, e={math.e:.3f}'

# Help for str
help(str)
