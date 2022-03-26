"""Converting celcius to fahrenheit v1
converting from degrees Celsius to Fahrenheit
function takes in a value, does the conversion and puts answer into a list
Wen-Qi Toh
26/3/22"""


def to_f(from_c):
    fahrenheit = (from_c * 9 / 5) + 32
    return fahrenheit


# main routine
temperature_list = [0, 40, 100]
converted = []

for temp in temperature_list:
    answer = to_f(temp)
    ans_statement = f"{temp} degrees C is {answer} degrees F"
    converted.append(ans_statement)

print(converted)
