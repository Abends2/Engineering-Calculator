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
        # Удаление нуля
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

    def add_functions():
        return 0

    # Function of main calculate (without eng_functions)
    def calculate():
        value = entry.get()
        # Если вводим, например, 7 * и потом нажимаем равно, то будет 7 * 7, т.е 49
        if value[-1] in '+-*/':
            value = value + value[:-1]
        entry.delete(0, END)
        entry.insert(0, eval(value))

    def cleaning_by_ac():
        entry.delete(0, END)

    def remove_last_elem_by_del():
        entry.delete(len(entry.get()) - 1)

    # creating buttons
    def creating_buttons_on_window():
        # names of buttons
        functions = ['sin', 'cos', 'tan', 'sqrt',
                     'fact', 'log', 'paw', 'exp']

        #staples = ['(', ')'] (LS, RS)

        numbers = ['7', '8', '9',
                   '4', '5', '6',
                   '1', '2', '3',
                   '0']

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

        RS = Button(window, text='(', width=3, command=lambda: add_digit('('),
                     bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
        RS.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)

        LS = Button(window, text=')', command=lambda: add_digit(')'), width=3,
                    bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
        LS.grid(row=row, column=col + 1, ipadx=11, ipady=10, padx=10, pady=12)

        DEL = Button(window, text='DEL', width=3, command=remove_last_elem_by_del,
                         bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
        DEL.grid(row=row, column=col+2, ipadx=11, ipady=10, padx=10, pady=12)

        AC = Button(window, text='AC', command=cleaning_by_ac, width=3,
                            bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
        AC.grid(row=row, column=col+3, ipadx=11, ipady=10, padx=10, pady=12)

        for k in numbers:
            b_numbers = Button(window, text=k, command=lambda x=k: add_digit(x),
                               width=3, bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
            b_numbers.grid(row=row+1, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # creating result and dot without array
        dot_btn = Button(window, text='.', width=3, command=lambda: add_digit('.'),
                               bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
        dot_btn.grid(row=row+1, column=col, ipadx=11, ipady=10, padx=10, pady=12)

        result_btn = Button(window, text='=', command=calculate, width=3,
                               bg='#635c57', fg='#40C3EC', borderwidth=5, font=f1)
        result_btn.grid(row=row+1, column=col+1, ipadx=11, ipady=10, padx=10, pady=12)

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
