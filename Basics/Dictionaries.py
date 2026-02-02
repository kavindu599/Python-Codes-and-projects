customer = {
    "Name": "John Smith",
    "Age": 30,
    "is_verified": True
}

print(customer["Name"])

print(customer["Age"])

print(customer.get("birthdate", "Jan 1 1980"))

# dictionary Exercise

phone = input("Phone: ")

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}

output = ""

for ch in phone:
    output += digits_mapping.get(ch, "!")+" "

print(output)



