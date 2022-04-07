"""Component 8 - Output Calculation History to Text File v1
basic printing each item in data list on the same line
Source: https://www.quru99.com/reading-and-writing-files-in-python.html
Wen-Qi Toh
7/4/22"""

# data to be outputted
data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# get filename, can't be blank / invalid
# assume valid data for now
filename = input("Enter a Filename: ")

# create file to hold data
f = open(filename, "w+")

for item in data:
    f.write(item)

# close file
f.close()
