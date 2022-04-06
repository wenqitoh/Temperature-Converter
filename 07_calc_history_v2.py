""" Component 7 - calculation history v2 trial 2
add calculations to list, output recent 3
trial 2 - use a deque method
Wen-Qi Toh
29/3/22"""

from collections import deque
calculations = deque()

# get give items of data
for item in range(0, 5):
    get_item = input("Enter an item: ")

    # add items to start of 'list'
    calculations.appendleft(get_item)

# show that everything made it to the list
print()
print("***** The Full List *****")
print(calculations)

print()

print("***** Most Recent 3 *****")
for item in range(0, 3):
    print(calculations[item])
