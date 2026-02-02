numbers = [2,3,4,5,5,7,8,9,9,1,1]

unique = []

for number in numbers:
    if number not in numbers:
        unique.append(number)
print(unique)