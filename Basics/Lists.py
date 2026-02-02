names = ['John', 'Bob', 'Mosh', 'sarah', 'Mary']
print(names)

# Access the list
print(names[0])
print(names[2])
print(names[-1])
print(names[-2])

print(names[2:])
print(names[2:4])
print(names[:])

# modify items
names[0] = 'Jone'
print(names)

# to find the largest number in a list

numbers = [2,6,21,65,32,66,87,87,92,65.90]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
print(max_number)

# list oprations

# add items
numbers.insert(0,10)
print(numbers)

# remove items
numbers.remove(6)
print(numbers)

# to clear the list use clear()

# to remove the last item in the list
numbers.pop()
print(numbers)

# check for a axistence of an item
print(numbers.index(65))

#check for a axistence of an item using in
print(65 in numbers)

# count the same item in the list
print(numbers.count(87))

# sort the list in ascending order
numbers.sort()
print(numbers)

# sort the list in descending order
numbers.reverse()
print(numbers)

# copy the list

numbers2 = numbers.copy()
numbers2.append(33)
print(numbers)
print(numbers2)

