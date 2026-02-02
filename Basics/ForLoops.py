for number in range(3):
    print("Attempt", number+1, (number +1)*".")

print("\n")

for number in range(1, 4):
    print("Attempt", number, number * ".")

print("\n")

for number in range(1,10,2):
    print("Attepmpt", number, number*".")


print("\n")

# for and else

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 time and Failed")