
# for number in range(1, 10, 2):
# print("Attempt", number + 1, (number + 1) * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print(type(5))
print(type(range(5)))
# While loops
number = 100
while number > 0:
    print(number)
    number = number // 2

"""
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)
"""
# Functions


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("John")

# keyword argument


def increment(number, by):
    return number + by


result = increment(number=2, by=1)
print(result)

# default argument


def increment2(number, by=1):
    return number + by


result2 = increment2(number=2)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(2, 3, 4, 5))
