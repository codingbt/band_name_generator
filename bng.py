
# This is a band name generator

name = input("What is your name?\n")
address = input("What is you address?\n")
age = input("How old are you?\n")


def new_line():
    print("\n")


new_line()


def personal_info():
    print(name)
    print(address)
    print(age)


personal_info()

new_line()

# Nesting Variables Logic
computer_name = input("What is the brand of your computer?\n")
length = len(computer_name)
print(length)
