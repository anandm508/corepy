"""Run the contents in the REPL python promt"""
import time
# Experimenting with immutable objects
a = 498
# Id returns an unique integer identifier for an object that is constant for the life of the object
id(a)

b = 1729
id(b)

b = a
id(b)

id(a) == id(b)

a is b  # Similar to statement above

a is None

t = 5
id(t)
t += 2
id(t)

# Experimenting with mutable object
r = [1, 2, 3]
s = [1, 2, 3]
# Content is equal, will return true
r == s
# r and s both are different objects, hence will be false
r is s
s = r
s[2] = 55
r

m = [9, 15, 24]


def modify(m):
    m.append(2)
    return m


modify(m)


def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)


banner("India is great")
banner("India is great", "*")
banner("India is great", border="*")
banner(message="India is great", border="*")
banner(border="*", message="India is great")

# Default arguments are evaluated once when def is evaluated
time.ctime()


def show_default(arg=time.ctime()):
    print(arg)


# Will give the same output
show_default()
show_default()
show_default()


def add_ghee(menu=[]):
    """Since defaults are constructed once, 
    multiple invocation without menu will result in error prone state"""
    menu.append("Ghee")
    return menu


add_ghee(['makke di roti', 'sarso da saag'])
add_ghee()
add_ghee()
add_ghee()
add_ghee()
add_ghee()
add_ghee()


def add_ghee_v1(menu=None):
    """Uses immutable None and will construct a new list when the default is deployed"""
    if menu is None:
        menu = []
    menu.append("Ghee")
    return menu


add_ghee_v1(['makke di roti', 'sarso da saag'])
add_ghee_v1()
add_ghee_v1()
add_ghee_v1()
add_ghee_v1()
add_ghee_v1()
add_ghee_v1()

# Python dynamic typing


def add(a, b):
    return a + b


add(1, 3)
add(1.5, 5.8)
add("Hello", "World")
add([1, 2], [3, 4])


# Demo of G from LEGB
# Rebinding global names

count = 0


def show_count():
    return count


def set_count(c):
    # Without "global count" the variable count outside def wont be reffered
    global count
    count = c


# Inspect the type of objects
type(1)
type(1.56)
type("Anand")
type([1, 2, 3])
type({"anand": "9163034500", "ekta": "9905595500"})
