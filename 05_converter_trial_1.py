"""Component 5 - converter trial 1
based on 02_Converter_GUI_v1
added commands to buttons - line 51, 57
added functions for each conversion -lines 82-94
Wen-Qi Toh
26/3/21"""

from tkinter import*
from functools import partial   # to prevent unwanted additional windows
import random


class Converter:
    def __init__(self):
        # formatting variables
        bg_colour = "light blue"

        # converter frame
        self.converter_frame = Frame(width=300, bg=bg_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_lbl = Label(self.converter_frame,
                                      text="Temperature Converter",
                                      font="Arial 16 bold",
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.temp_heading_lbl.grid(row=0)

        # instructions (row 1)
        self.temp_instructions_lbl = Label(self.converter_frame,
                                           text="Type in the amount to be "
                                                "converted and then push one "
                                                "of the buttons below...",
                                           font="Arial 10 italic", wrap=250,
                                           justify=LEFT, bg=bg_colour,
                                           padx=10, pady=10)
        self.temp_instructions_lbl.grid(row=1)

        # temperature entry box (row 2)
        self.temp_entry = Entry(self.converter_frame, width=20,
                                font="Arial 14 bold")
        self.temp_entry.grid(row=2)

        # conversion buttons frame (row 3), orchid1, khaki 1
        self.conversion_btns_frame = Frame(self.converter_frame)
        self.conversion_btns_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_btns_frame, text="To Centigrade",
                                  font="arial 10 bold", command=self.to_cen, bg="Khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_btns_frame, text="To Fahrenheit",
                                  font="arial 10 bold", bg="Orchid1", command=self.to_far, padx=10, pady=10)
        self.to_f_button.grid(row=0, column=1)
        # answer label (row 4)
        self.converted_label = Label(self.converter_frame, font="Arial 14 bold",
                                     fg="purple", bg=bg_colour, pady=10,
                                     text="Conversion goes here")
        self.converted_label.grid(row=4)

        # history / help button frame (row 5)
        self.hist_help_frame = Frame(self.converter_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.calc_hist_button = Button(self.hist_help_frame,
                                       font="Arial 12 bold",
                                       text="Calculation History",
                                       width=15)
        self.calc_hist_button.grid(row=0, column=0)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def to_cen(self):
        which = 1
        self.change(which)

    def to_far(self):
        which = 2
        self.change(which)

    def change(self, which):
        if which == 1:
            print("Centigrade  result")
        else:
            print("Fahrenheit result")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
