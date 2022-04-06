""" Component 7 - calculation history v4
continuing with trial 3
add calculations to list, output recent 3 calculations
(no need for extra code or importing extra libraries)
Wen-Qi Toh
29/3/22"""

# set up empty list
all_calculations = []

# get items of data, add to list
get_item = ""
while get_item != "zz":
    get_item = input("Enter an item: ")

    if get_item == "zz":
        break

    all_calculations.append(get_item)

print()

if len(all_calculations) == 0:
    print("Oops - the list is empty")
else:
    # show that everything made it to the list...
    print()
    print("***** The Full List *****")
    print(all_calculations)

    # print items starting at the END of the list
    if len(all_calculations) >= 3:
        print("***** Most Recent 3 *****")
        for item in range(0, 3):
            print(all_calculations[len(all_calculations) - item - 1])
    else:
        print("*** items from newest to oldest ***")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index(item) - 1])
