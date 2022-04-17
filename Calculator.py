from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import math
import sys

# 40C3EC - color for text on Buttons
# fffff0 - background color
# 40C3EC - foreground color

window = Tk()
window.title('THE BEST CALC EVER')
window.geometry('345x750')
window.resizable(width=False, height=False)
window.configure(bg='#fffff0', borderwidth=8, relief='solid')

# set the font
f1 = font.Font(family='Calibri', size=12, weight='bold')

# entry unit
entry = Entry(window, width=52, relief='solid', borderwidth=2, fg='#40C3EC', bg='#635c57')
entry.grid(row=0, column=0, columnspan=4, ipady=55)


def calc(x):
    entry.insert(0, x)


# names of buttons
btn = ['sin', 'cos', 'tan', 'sqrt',
       'fact', 'log', 'paw', 'exp',
       '(', ')', 'AC', 'DEL',
       '7', '8', '9', '-',
       '4', '5', '6', '*',
       '1', '2', '3', '/',
       '0', '.', '=', '+']

# creating buttons
row = 1
col = 0
for i in btn:
    button = Button(window, text=i, command=lambda x=i: calc(x),
                    width=3, bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
    button.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)
    col += 1
    if col > 3:
        col = 0
        row += 1

# mainloop
window.grid_rowconfigure(0, weight=1)
window.mainloop()
