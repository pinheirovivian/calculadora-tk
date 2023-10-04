import tkinter as tk
from tkinter import *

numero1 = ''
numero2 = ''
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE

root = Tk()
root.title('calculadora')
root.geometry("500x400")
root.maxsize(500, 400)
root.minsize(500, 400)


root.configure(background='#EBEBEB')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFC928',
          bg='#EBEBEB', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)


def botao_click(num):
    e.insert(END, num)


def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_subrai():
    global numero1
    global subtracao
    subtracao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_divide():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)


def botao_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    numero2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2))
        divisao = FALSE


def botao_limpa():
    e.delete(0, END)


def botao_num(num, row, column):
    botao = Button(root,
                   text=num,
                   padx=40,
                   pady=20,
                   command=lambda: botao_click(num),
                    fg='#FFC928',
                    activebackground='#EBEBEB',
                    activeforeground='#FFC928',
                    bg='#011752',
                   relief=FLAT,
                   font=('futura', 12, 'bold'))
    botao.grid(row=row, column=column)


def botao_operador(op, command, row, column):
    operador = Button(root,
                      text=op,
                      padx=40,
                      pady=20,
                      command=command,
                      fg='#FFC928',
                      activebackground='#EBEBEB',
                      activeforeground='#FFC928',
                      bg='#011752',
                      relief=FLAT,
                      font=('futura', 12, 'bold'))
    operador.grid(row=row, column=column)


botao_operador('÷', botao_divide, 0, 4)
# primeira fileira
botao_num(1, 1, 1)
botao_num(2, 1, 2)
botao_num(3, 1, 3)
botao_operador('×', botao_multiplica, 1, 4)
# segunda fileira
botao_num(4, 2, 1)
botao_num(5, 2, 2)
botao_num(6, 2, 3)
botao_operador(' -', botao_subrai, 2, 4)
# terceira fileira
botao_num(7, 3, 1)
botao_num(8, 3, 2)
botao_num(9, 3, 3)
botao_operador('+', botao_adiciona, 3, 4)
# quarta fileira
zero = Button(root,
              text='0',
              padx=91,
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFC928',
              activebackground='#EBEBEB',
              activeforeground='#FFC928',
              bg='#011752',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2)
botao_operador('C', botao_limpa, 4, 4)
botao_operador('=', botao_igual, 4, 3)

root.mainloop()