"""Converting fahrenheit to celsius v1
converting from degrees Fahrenheit to Celsius
function takes in a value, does the conversion and puts answer into a list
Wen-Qi Toh
26/3/22"""


def to_c(from_f):
    celsius = (from_f - 32) * (5 / 9)
    return celsius


# main routine
temperature_list = [0, 32, 100]
converted = []

for temp in temperature_list:
    answer = to_c(temp)
    ans_statement = f"{temp} degrees F is {answer} degrees C"
    converted.append(ans_statement)

print(converted)
