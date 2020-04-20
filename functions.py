def square(x):
    return x*x


def launchMissiles():
    print("Missiles launched")


def even_or_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


def nth_root(radicand, n):
    return radicand ** (1/n)


def ordinal_suffix(value):
    s = str(value)
    if s.endswith('11'):
        return 'th'
    elif s.endswith('12'):
        return 'th'
    elif s.endswith('13'):
        return 'th'
    elif s.endswith('1'):
        return 'st'
    elif s.endswith('2'):
        return 'nd'
    elif s.endswith('3'):
        return 'rd'
    return 'th'


def ordinal(value):
    return str(value) + ordinal_suffix(value)


def display_nth_root(radicand, n):
    root = nth_root(radicand, n)
    message = "The " + ordinal(n) + " root of " \
        + str(radicand) + " is " + str(root)
    print(message)


print(square(5))
launchMissiles()

w = even_or_odd(10)
print(w is None)

print(nth_root(27, 3))

print(ordinal(5))
display_nth_root(8, 3)
