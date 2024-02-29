print("usage: addition, subtraction, multiplication and division")

N_one = int(input("Enter a number: "))
N_two = int(input("Enter another number: "))
symbol = input("Enter symbol: ")

if symbol == "addition":
    print(f"Your result is {N_one + N_two} ")
#    while symbol == "":
#        print("Please enter symbol")
elif symbol == "subtraction":
    print(f"Your result is {N_one - N_two} ")
#    while symbol == "":
#        print("Please enter symbol")
elif symbol == "multiplication":
    print(f"Your result is {N_one * N_two} ")
#    while symbol == "":
#        print("Please enter symbol")
elif symbol == "division":
    print(f"Your result is {N_one / N_two} ")
#    while symbol == "":
#        print("Please enter symbol")
else:
    print("Invalid")