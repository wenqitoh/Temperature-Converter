"""component 9 - History GUI v3
copying 01_history_GUI_v5 code, changing all 'help' to 'history'
Wen-Qi Toh
20/03/22"""
from tkinter import *
from functools import partial   # to prevent unwanted windows


class Converter:
    def __init__(self):

        # formatting variable...
        bg_colour = "light blue"

        # initialise list to hold calculation history
        # in later versions list will be populated with user calculations
        self.all_calculations = ["0 degrees F is -17.8 degrees C",
                                 "0 degrees C is 32 degrees F",
                                 "40 degrees F is 4.4 degrees C",
                                 "40 degrees C is 104 degrees F",
                                 "12 degrees C is 53.6 degrees F",
                                 "24 degrees C is 75.2 degrees F",
                                 "100 degrees F is 37.8 degrees C"]

        # converter main screen GUI
        self.converter_frame = Frame(width=300, height=300, bg=bg_colour,
                                     padx=10, pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame,
                                          text="Temperature Converter",
                                          font=("Arial", 16, "bold"),
                                          bg=bg_colour, padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history button (row 1)
        self.history_button = Button(self.converter_frame, text="History",
                                     font=("Arial", 14), padx=10, pady=10,
                                     command=self.history)
        self.history_button.grid(row=1)

    def history(self):
        print("You asked for history")
        get_history = History(self)
        get_history.history_text.configure(text="history text goes here")


class History:
    def __init__(self, partner):
        background = "#a9ef99"  # pale green

        # disable history button
        partner.history_button.config(state=DISABLED)

        # set up child window (ie history box)
        self.history_box = Toplevel()

        # if users press cross at top, closes history and 'releases' history button
        self.history_box.protocol("WM_DELETE_WINDOW", partial(self.close_history,
                                                              partner))
        # set up GUI frame
        self.history_frame = Frame(self.history_box, width=300, bg=background)
        self.history_frame.grid()

        # set up history heading(row 0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame,
                                  text="Here are your most recent "
                                       "calculations. Please use the export "
                                       "button to create a text file of all "
                                       "your calculations for this session.",
                                  font="arial 10 italic", justify=LEFT,
                                  width=40, bg=background,
                                  wrap=250, fg="maroon", padx=10, pady=10)
        self.history_text.grid(row=1)

        # History output goes here... (row 2)

        # Export/Dismiss buttons frame (row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # export button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="arial 12 bold")
        self.export_button.grid(row=0, column=0)

        # dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 12 bold",
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = Converter()
    root.mainloop()
