"""
This is copied from the word document in student resources
"""

from tkinter import *
import random


class Foo:
    def __init__(self, parent):
        print("Hello World")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("title goes here")
    something = Foo(root)
    root.mainloop()
