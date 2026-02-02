# there are two types of functions

# 1- perform a task
# 2- return a value

# create a simple function
# 1- perform a task

def greet():
    print("Hi There!")
    print("Wlecome aboard!!")

greet()

def greet1(first_name, last_name):
    print(f"His {first_name}, {last_name}")
    print("welcome abroad!!")

greet1("kavindu", "Madusara")
greet1("Jeason", "Brody")


# there are two types of functions

# 1- perform a task
# 2- return a value

# 2- return a value

def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("kavindu")
print(message)
