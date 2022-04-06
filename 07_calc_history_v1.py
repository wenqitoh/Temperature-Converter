""" Component 7 - calculation history v1 trial 1
add calculations to list, output recent 3
trial 1 - use a list with reverse ordering
Wen-Qi Toh
29/3/22"""

# set up empty list
all_calculations = []

# get give items of data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

all_calculations.reverse()

# show that everything made it to the list...
print()
print("***** The Full List *****")
print(all_calculations)

print()

print("***** Most Recent 3 *****")
for item in range(0, 3):
    print(all_calculations[item])
