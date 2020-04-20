"""Dictionaries
key must me immutable like string
value could be mutable
Items in dictionary are not stored in any particular order
"""
from pprint import pprint
urls = {'google': 'http://google.com',
        'microsoft': 'http://microsoft.com',
        'pluralsight': 'http://pluralsight.com'}

urls['pluralsight']

# Creating a dictionary with a list of tuple and dict constructor
name_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 22), ('Daniel', 56)]
d = dict(name_and_ages)
d
# Another format
phonetic = dict(a='alfa', b='bravo', c='charlie', d='delta', e='echo')
phonetic


# As seen with list, copy is shallow by default
# Copy with copy function
phonetic_copy = phonetic.copy()
phonetic_copy
phonetic_copy is phonetic
phonetic_copy == phonetic

# Copy with dict constructor
phonetic_copy = dict(phonetic)
phonetic_copy
phonetic_copy is phonetic
phonetic_copy == phonetic

# Updating dictionary with another dictionary
# Replaces existing and adds new
stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
stocks.update({'GOOG': 894, 'YHOO': 25})
stocks

# Iteration
for key in stocks:
    print(f'key={key} => value={stocks[key]}')

for key in stocks.keys():
    print(key)

for value in stocks.values():
    print(value)


for key, value in stocks.items():
    print(f'key={key} => value={value}')


# Exploring in and not in
'GOOG' in stocks
'EXIDE' not in stocks

# Deleting
del stocks['GOOG']
stocks

# Dictinaory of element symbols with different isotopes
m = {'H': [1, 2, 3],
     'He': [3, 4],
     'Li': [6, 7],
     'Be': [7, 9, 10]}

# Updating key 'H'
m['H'] += [10, 11]
m

# Print using ppprint module
pprint(m)
