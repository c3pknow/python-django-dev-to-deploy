# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create a Function
def sayHello(name = 'Buster'):
    """
    Prints Hello, followed by name.
    """
    print(f'Hello {name}')

sayHello('Brian')
sayHello()


# Return Value
def getSum(num1, num2):
    return num1 + num2

print(getSum(3,5))
sum = getSum(3,87)
print(sum)


def addOneToNum(num):
    return num + 1
print(addOneToNum(44))

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions

getSum = lambda num1, num2 : num1 + num2
print(getSum(9,3))