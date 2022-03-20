"""component 1 - Help GUI, v1
Wen-Qi Toh
17/03/22"""

from tkinter import *
import random


class Converter:
    def __init__(self):
        print("Hello world")

        # formatting variable...
        bg_colour = "light blue"

        # converter main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=bg_colour)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=bg_colour, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
