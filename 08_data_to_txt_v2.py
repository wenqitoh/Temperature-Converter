"""Component 8 - Output Calculation History to Text File v2
printing each data item on a new line
Source: https://www.quru99.com/reading-and-writing-files-in-python.html
Wen-Qi Toh
7/4/22"""

# data to be outputted
data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

# get filename, can't be blank / invalid
# assume valid data for now
filename = input("Enter a Filename (leave off the extension): ")

# add .txt suffix!
filename = filename + ".txt"
# create file to hold data
f = open(filename, "w+")

# add new line at end of each item
for item in data:
    f.write(item + "\n")

# close file
f.close()
