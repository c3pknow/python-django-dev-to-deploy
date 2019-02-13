# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
fruit_tuple = ('Apple', 'Orange', 'Mango')
# fruit_tuple = tuple(('Apple', 'Orange', 'Mango'))
print(fruit_tuple)

# Get Single Value
print(fruit_tuple[2])

# CANNONT CHANGE VALUE
# fruit_tuple[1] = 'Grape'

# TUPLE WITH 1 VALUE SHOULD HAVE A TRAILING COMMA
fruit_tuple_2 = ('Apple',)
print(fruit_tuple_2)

# Length
print(len(fruit_tuple))
print(len(fruit_tuple_2))

# Delete a tuple
del fruit_tuple_2


# A Set is a collection which is unordered and unindexed. No duplicate members.
vegetables = {'Zucchini', 'Onion', 'Spinach', 'Pepper', 'Onion'}
print(vegetables)

# Check if in set
print('Pepper' in vegetables)

# Add to set
vegetables.add('Broccoli')
print(vegetables)

# Remove from Set
vegetables.remove('Spinach')
print(vegetables)

# Clear Set
vegetables.clear()

# Delete Set
del vegetables
