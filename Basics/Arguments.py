# keyword arguments

def increment(number, by):
    return number + by

print(increment(number = 12, by = 4))

# this way codes are more readable and understandable



# default arguments

def increment1 (numbers, add = 3):
    return numbers+add

print(increment1(11,6))


# x arguments

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply(2,3,4,5,6))
    