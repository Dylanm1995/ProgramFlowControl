name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))

if age >= 18 and age < 31:
    print("Enjoy your holiday")
elif age < 18:
    print("Sorry you're too young to come on holiday, {0}".format(name))
else:
    print("Sorry you're too old to come on holiday")