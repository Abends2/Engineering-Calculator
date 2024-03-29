from tkinter import *
import tkinter.font as font
import math
import sys

# 40C3EC - цвет текста на кнопках
# fffff0 - цвет фона
# 0a0a0a - фон окна ввода/вывода


def main():
    # Основная конфигурация окна
    window = Tk()
    window.title("Engineering Calculator")
    window.iconbitmap(r'.\assets\icon.ico')
    window.geometry('345x750')
    window.resizable(width=False, height=False)
    window.configure(bg='#fffff0', borderwidth=8, relief='solid')

    # Шрифты
    f1 = font.Font(family='Calibri', size=12, weight='bold')
    f2 = font.Font(family='Arial', size=16, weight='bold')

    # Окно ввода/вывода и его конфигурация
    entry = Entry(window, width=26, relief='solid', borderwidth=2, fg='#40C3EC', bg='#0a0a0a', justify=RIGHT, font=f2)
    entry.insert(0, '0')
    entry.grid(row=0, column=0, columnspan=4, ipady=55)

    # Добавление цифр
    def add_digit(digit):
        value = entry.get() + str(digit)
        if value[0] == '0':
            value = value[1:]
        entry.delete(0, END)
        entry.insert(0, value)

    # Добавдение операционных символов
    def add_operation(operation):
        value = entry.get()
        if value[-1] in '+-*/':
            value = value[:-1]
        entry.delete(0, END)
        entry.insert(0, value + operation)

    # Функция для вычисления математических функций
    def add_functions(x):
        value = entry.get()
        if x == 'sin':
            str(entry.insert(0, 'sin')) + str(entry.insert(END, ' = ' + str(math.sin(float(value)))))
        elif x == 'cos':
            str(entry.insert(0, 'cos')) + str(entry.insert(END, ' = ' + str(math.cos(float(value)))))
        elif x == 'tan':
            str(entry.insert(0, 'tan')) + str(entry.insert(END, ' = ' + str(math.tan(float(value)))))
        elif x == 'sqrt':
            str(entry.insert(0, '√')) + str(entry.insert(END, ' = ' + str(math.sqrt(float(value)))))
        elif x == 'fact':
            str(entry.insert(0, 'fact')) + str(entry.insert(END, ' = ' + str(math.factorial(int(value)))))
        elif x == 'ln':
            str(entry.insert(0, 'ln')) + str(entry.insert(END, ' = ' + str(math.log10(float(value)))))
        elif x == 'pow':
            entry.insert(END, "**")
        elif x == 'exp':
            str(entry.insert(0, 'e^')) + str(entry.insert(END, ' = ' + str(math.exp(float(value)))))
        else:
            sys.exit()

    # Функция для базовых вычислений (+ - * /)
    def calculate():
        value = entry.get()
        if value[-1] in '+-*/':
            value = value + value[:-1]
        entry.delete(0, END)
        entry.insert(0, eval(value))

    # Функция удаления (кнопка AC)
    def cleaning_by_ac():
        entry.delete(0, END)

    # Функция удаления (кнопка DEL)
    def remove_last_elem_by_del():
        entry.delete(len(entry.get()) - 1)

    # Создание кнопок
    def creating_buttons_on_window():
        functions = ['sin', 'cos', 'tan', 'sqrt',
                     'fact', 'ln', 'pow', 'exp']

        numbers = ['7', '8', '9',
                   '4', '5', '6',
                   '1', '2', '3',
                   '0']

        operations = ['-', '+', '*', '/']

        # Размещаем кнопки
        row = 1
        col = 0
        for i in functions:
            b_functions = Button(window, text=i, command=lambda x=i: add_functions(x), width=3,
                                 bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
            b_functions.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1
            if col > 3:
                col = 0
                row += 1

        right_bracket = Button(window, text='(', width=3, command=lambda: add_digit('('),
                               bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
        right_bracket.grid(row=row, column=col, ipadx=11, ipady=10, padx=10, pady=12)

        left_bracket = Button(window, text=')', command=lambda: add_digit(')'), width=3,
                              bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
        left_bracket.grid(row=row, column=col + 1, ipadx=11, ipady=10, padx=10, pady=12)

        btn_del = Button(window, text='DEL', width=3, command=remove_last_elem_by_del,
                         bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
        btn_del.grid(row=row, column=col+2, ipadx=11, ipady=10, padx=10, pady=12)

        btn_ac = Button(window, text='AC', command=cleaning_by_ac, width=3,
                        bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
        btn_ac.grid(row=row, column=col+3, ipadx=11, ipady=10, padx=10, pady=12)

        for k in numbers:
            b_numbers = Button(window, text=k, command=lambda x=k: add_digit(x),
                               width=3, bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
            b_numbers.grid(row=row+1, column=col, ipadx=11, ipady=10, padx=10, pady=12)
            col += 1
            if col > 2:
                col = 0
                row += 1

        dot_btn = Button(window, text='.', width=3, command=lambda: add_digit('.'),
                         bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
        dot_btn.grid(row=row+1, column=col, ipadx=11, ipady=10, padx=10, pady=12)

        result_btn = Button(window, text='=', command=calculate, width=3,
                            bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
        result_btn.grid(row=row+1, column=col+1, ipadx=11, ipady=10, padx=10, pady=12)

        row = 4
        for t in operations:
            b_operations = Button(window, text=t, command=lambda x=t: add_operation(x), width=3,
                                  bg='#0a0a0a', fg='#40C3EC', borderwidth=5, font=f1)
            b_operations.grid(row=row, column=3, ipadx=11, ipady=10, padx=10, pady=12)
            row += 1

    creating_buttons_on_window()
    window.grid_rowconfigure(0, weight=1)
    window.mainloop()


if __name__ == "__main__":
    main()
