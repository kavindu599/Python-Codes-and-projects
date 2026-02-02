# and
# or
# not

# application for processing loans

high_income = True
good_credit = True
Student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if high_income or good_credit:
    print("Eligible")
else:
    print("Not Eligible")


if not Student:
    print("Eligible")
else:
    print("Not Eligible")


if (high_income or good_credit) and not Student:
    print("Eligible")
else:
    print("Not Eligible")