"""Component 6 - converter v2
copy of 05_converter_trial_2v2, with updates
building on to_convert function, incorporating pre-made functions and code
Wen-Qi Toh
26/3/21"""

from tkinter import*


class Converter:
    def __init__(self):

        # formatting variables
        bg_colour = "light blue"

        # converter frame
        self.converter_frame = Frame(bg=bg_colour, pady=10)
        self.converter_frame.grid()

        # temperature converter heading (row 0)
        self.temp_heading_lbl = Label(self.converter_frame,
                                      text="Temperature Converter",
                                      font="Arial 19 bold",
                                      bg=bg_colour,
                                      padx=10, pady=10)
        self.temp_heading_lbl.grid(row=0)

        # instructions (row 1)
        self.temp_instructions_lbl = Label(self.converter_frame,
                                           text="Type in the amount to be "
                                                "converted and then push one "
                                                "of the buttons below...",
                                           font="Arial 10 italic", wrap=290,
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
                                  font="arial 10 bold",
                                  command=lambda: self.temp_convert(-459),
                                  bg="Khaki1", padx=10, pady=10)
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_btns_frame, text="To Fahrenheit",
                                  font="arial 10 bold",
                                  command=lambda: self.temp_convert(-273),
                                  bg="Orchid1", padx=10, pady=10)
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

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf"   # pale pink bg for when entry box has errors

        # retrieve amount entered into Entry field
        to_convert = self.temp_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            # check amount is valid, convert to F
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = f"{to_convert} degrees C is {fahrenheit} degrees F"

            # check amount is valid, convert to C
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = f"{to_convert} degrees F is {celsius} degrees C"

            else:
                # if input is invalid (eg too cold)
                answer = "too cold!"
                has_errors = "yes"

            # display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.temp_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.temp_entry.configure(bg=error)

            # add answer to history list

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.temp_entry.configure(bg=error)
            # round!!

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round, 1)
        return rounded


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
