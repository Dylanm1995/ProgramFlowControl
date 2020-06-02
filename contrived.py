numbers = [1, 45, 21, 16, 60]

for number in numbers:
    if number % 8 == 0:
        # reject the list
        print("The numbers are unacceptable")
        break

else:
    print("The numbers are fine")