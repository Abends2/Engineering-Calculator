from tkinter import *
import math

# #40C3EC - цвет для текста кнопок
# #fffff0 - bg
# #40C3EC - fg

window = Tk()
window.title("THE BEST CALC EVER")
window.geometry('355x750')
window.resizable(width=False, height=False)
window.configure(bg='#fffff0', borderwidth=8, relief="solid")

btn = ['sin', 'cos', 'tan', 'sqrt',
       'fact', 'log', 'paw', 'exp',
       '(', ')', 'AC', 'DEL',
       '7', '8', '9', '-',
       '4', '5', '6', '*',
       '1', '2', '3', '/',
       '0', '.', '=', '+']

count = 0
for i in range(7):
    for j in range(4):
        b = Button(window, text=btn[count], width=3, bg='#635c57', fg='#40C3EC', font=("Calibri 12 bold"), borderwidth=5)
        b.grid(row=i + 1, column=j, ipadx=10, ipady=10, padx=12, pady=12)
        count += 1

window.grid_rowconfigure(0, weight=1)
window.mainloop()
