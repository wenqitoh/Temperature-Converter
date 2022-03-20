"""component 1 - Help GUI, v2
Wen-Qi Toh
19/03/22"""
from tkinter import *


class Converter:
    def __init__(self):

        # formatting variable...
        bg_colour = "light blue"

        # converter main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=bg_colour,
                                     padx=10, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=bg_colour, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # help button (row 1)
        self.help_button = Button(self.converter_frame, text="Help",
                                  font=("Arial", "14"), padx=10, pady=10)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help")
        get_help = Help()
        get_help.help_text.configure(text="Help text goes here")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
