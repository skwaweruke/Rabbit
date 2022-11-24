#   use eval function to accept only number.
#   getting input from user using input function

name = input("Enter your name: ")

#   name = eval(input("Enter your name: "))


print("You typed", name)

if name == "simon":
    print("You entered a text.")
if name != "simon":
    print("Your input is a number.")
