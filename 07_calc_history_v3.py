""" Component 7 - calculation history v3 trial 3
add calculations to list, output recent 3 calculations
use a list with reverse ordering
(no need for extra code or importing extra libraries)
Wen-Qi Toh
29/3/22"""

# set up empty list
all_calculations = []

# get give items of data
for item in range(0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

# show that everything made it to the list...
print()
print("***** The Full List *****")
print(all_calculations)

print()

print("***** Most Recent 3 *****")
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])
