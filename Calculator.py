from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import math

# 40C3EC - color for text on Buttons
# fffff0 - background color
# 40C3EC - foreground color


def main():
    # window's settings
    window = Tk()
    window.title("Engineering Calculator")
    window.iconbitmap('./assets/icon.ico')
    window.geometry('345x750')
    window.resizable(width=False, height=False)
    window.configure(bg='#fffff0', borderwidth=8, relief='solid')

    # set fonts
    f1 = font.Font(family='Calibri', size=12, weight='bold')
    f2 = font.Font(family='Arial', size=16, weight='bold')

    # entry unit and his settings
    entry = Entry(window, width=26, relief='solid', borderwidth=2, fg='#40C3EC', bg='#635c57', justify=RIGHT, font=f2)
    entry.insert(0, '0')
    entry.grid(row=0, column=0, columnspan=4, ipady=55)

    # Function 1
    def add_digit(digit):
        value = entry.get() + str(digit)
        if value[0] == '0':
            value = value[1:]
        entry.delete(0, END)
        entry.insert(0, value)

    # Function 2
    def add_operation(operation):
        value = entry.get()
        if value[-1] in '+-*/':
            value = value[:-1]
        entry.delete(0, END)
        entry.insert(0, value + operation)

    # creating buttons
    def creating_buttons_on_window():
        # names of buttons
        functions = ['sin', 'cos', 'tan', 'sqrt',
                     'fact', 'log', 'paw', 'exp']

        addons = ['(', ')', 'AC', 'DEL']

        numbers = ['7', '8', '9',
                   '4', '5', '6',
                   '1', '2', '3',
                   '0']

        result_and_dot = ['.', '=']

        operations = ['-', '+', '*', '/']

        # Now, we can place our buttons on window
        row = 1
        col = 0
        for i in functions:
            b_functions = Button(window, text=i, command=lambda x=i: add_digit(x), width=3,
                                 bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
            b_functions.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1
            if col > 3:
                col = 0
                row += 1

        for j in addons:
            b_addons = Button(window, text=j, command=lambda x=j: add_digit(x), width=3,
                              bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
            b_addons.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1
            if col > 3:
                col = 0
                row += 1

        for k in numbers:
            b_numbers = Button(window, text=k, command=lambda x=k: add_digit(x),
                               width=3, bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
            b_numbers.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1
            if col > 2:
                col = 0
                row += 1

        for r in result_and_dot:
            b_numbers = Button(window, text=r, command=lambda x=r: add_digit(x), width=3,
                               bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
            b_numbers.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1

        row = 4    # Переопределяем для нового отсчета (операции надо хуйнуть в столбик)
        for t in operations:
            b_operations = Button(window, text=t, command=lambda x=t: add_operation(x), width=3,
                                  bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
            b_operations.grid(row=row, column=3, ipadx=11, ipady=10, padx=10, pady=12)
            row += 1

    creating_buttons_on_window()
    window.grid_rowconfigure(0, weight=1)
    window.mainloop()


# mainloop
if __name__ == "__main__":
    main()
