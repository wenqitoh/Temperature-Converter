"""component 4 - number checking function
does not accept temperatures lower than -273C or -459F, produces error sign
Wen-Qi Toh
26/3/22"""

# code to check that a number is valid
def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))
            if response < low:
                print("Too cold!")
            else:
                return response
        except ValueError:
            print("Please enter a number! ")

# main routine
# set up to run this code twice (for two valid responses in test plan)
number = temp_check(-273)
print("You entered {}".format(number))

number = temp_check(-459)
print("You entered {}".format(number))
