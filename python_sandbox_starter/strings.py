# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Brian'
age = 38

# String Formatting
# Concatenate
print ('Hello I am ' + name + ' and I am ' + str(age))

# Arguments by position
print('{}, {}, {}'.format('a',  'b', 'c'))
print('{1}, {0}, {2}'.format('a',  'b', 'c'))

# Arguments by name
print ('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (only in 3.6+)
print(f'My name is {name} and O am {age}')


# String Methods
s = 'hello there world'

# Capitalize first letter
print(s.capitalize())

# All Uppercase
print(s.upper())

# All lowercase
print(s.lower())

# Swap Case
print(s.swapcase())

# Length of string
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count 'h' in string
sub = 'h'
print(s.count(sub))

# Starts With
print(s.startswith('hello'))

# Ends With
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find Position
print(s.find('r'))

# Is Alphanumeric
print(s.isalnum())

# Is Alphabetical
print(s.isalpha())

# Is Numeric
print(s.isnumeric())
