t = [21, 56454, 98987989, 656598989]

for p in enumerate(t):
    print(p)

# Or even better use the tuple unpacking with f string
for k, v in enumerate(t):
    print(f'k = {k}, v = {v}')
