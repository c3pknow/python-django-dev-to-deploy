# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}
print(person)

# person2 = dict(
#     first_name = 'John',
#     last_name = 'Doe',
#     age = 30
# )
# print(person2)

# Access Value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get Keys
print(person.keys())

# Get Items with keys and values
print(person.items())

# Get Length
print(len(person))

# Copy
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

# Delete key/value
del(person['age'])
print(person)

# Pop (same as delete)
person.pop('phone')
print(person)

# Clear dictionary
person.clear()
print(person)

# List of Dictionaries
people = [
    {'name': 'Martha', 'age': 44},
    {'name': 'Dave', 'age': 30}
]
print(people)
print(people[1]['name'])