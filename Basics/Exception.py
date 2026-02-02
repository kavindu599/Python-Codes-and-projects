try:
    age = int(input("Age: "))
    income = 50000
    risk = income / age
    print(age)
except ValueError:
    print("Invlaid Value")

except ZeroDivisionError:
    print("Age Can't be Zero")

