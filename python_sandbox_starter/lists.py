# A List is a collection which is ordered and changeable. Allows duplicate members.

numbers = [1,2,3,4,5,6,7]
print(type(numbers))
print(numbers)

digits = list((1,2,3,4,5))
print (digits)

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears', 'Bananas']

# Get value by index
print(fruits[2])

# Get Length
print(len(fruits))

# Append to List
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from position
fruits.pop(3)
print(fruits)

# Reverse List
fruits.reverse()
print(fruits)

# Sort 
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
