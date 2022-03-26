"""Component 4 - rounding trial 1
testing for an effective and efficient way to round temperature values
Wen-Qi Toh
26/3/22"""

# display output using rounding for floats only

to_round = [1/1, 1/2, 1/3]
print("***** numbers to round *****")
print(to_round)

print()
print("***** rounded numbers *****")

for num in to_round:
    if num.is_integer():
        print("{:.0f}". format(num))
    else:
        print("{:.1f}".format(int(num)))
