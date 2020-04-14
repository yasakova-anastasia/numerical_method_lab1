from matplotlib import pyplot as plt
import pylab
from tkinter import *
from tkinter.ttk import Combobox
import math

def decision(event):
    x0 = event.xdata
    y0 = event.ydata # получение начальных условий

    x = []
    y = []

    global a, b, c, h, count 
    count = 0

    t_i = a
    x_i = x0
    y_i = y0

    i = a
    while (i <= b):
        k11 = h * y_i
        k12 = h * (-math.sin(x_i) - c * y_i)

        k21 = h * (y_i + k12/2)
        k22 = h * (-math.sin(x_i + k11 / 2) - c * (y_i + k12 / 2))

        k31 = h * (y_i + k22 / 2)
        k32 = h * (-math.sin(x_i + k21 / 2) - c * (y_i + k22 / 2))

        k41 = h * (y_i + k32 / 2)
        k42 = h * (-math.sin(x_i + k31 / 2) - c * (y_i + k32 / 2))

        x_i = x_i + 1/6 * (k11 + 2 * k21 + 2 * k31 + k41)
        y_i = y_i + 1/6 * (k12 + 2 * k22 + 2 * k32 + k42)

        x.append(x_i)
        y.append(y_i)
        i = i + h

    global x_, y_
    x_ = x.pop()
    x.append(x_)
    y_ = y.pop()
    y.append(y_)

    plt.plot(x, y)
    plt.show()


def continue_(event):
    global a, b, c, h, x_, y_, count
    count = count + 1
    t_i = b * count
    x_i = x_
    y_i = y_

    x = []
    y = []

    i = t_i
    while (i <= b * (count + 1)):
        k11 = h * y_i
        k12 = h * (-math.sin(x_i) - c * y_i)

        k21 = h * (y_i + k12/2)
        k22 = h * (-math.sin(x_i + k11 / 2) - c * (y_i + k12 / 2))

        k31 = h * (y_i + k22 / 2)
        k32 = h * (-math.sin(x_i + k21 / 2) - c * (y_i + k22 / 2))

        k41 = h * (y_i + k32 / 2)
        k42 = h * (-math.sin(x_i + k31 / 2) - c * (y_i + k32 / 2))

        x_i = x_i + 1/6 * (k11 + 2 * k21 + 2 * k31 + k41)
        y_i = y_i + 1/6 * (k12 + 2 * k22 + 2 * k32 + k42)

        x.append(x_i)
        y.append(y_i)
        i = i + h

    x_ = x.pop()
    x.append(x_)
    y_ = y.pop()
    y.append(y_)

    plt.plot(x, y)
    plt.show()



def entry(_a, _b, _c, _h):
    fig, ax = plt.subplots()
    global a, b, c, h
    a = _a
    b = _b
    c = _c
    h = _h

    id1 = fig.canvas.mpl_connect('button_press_event', decision) # клик мыши для начальных условий
    id2 = fig.canvas.mpl_connect('key_press_event', continue_) # нажатие клавиши для продолжения траектории

    plt.tight_layout()
    plt.axis([-10, 10, -10, 10])
    plt.show()



x0 = 0
y0 = 0
root = Tk() # создание графического окна
root.title("Ввод информации") 
root.geometry("600x300") # размер окна


label1 = Label(text = "x'' + δ * x' + sin(x) = 0", font = "Arial 14")
label2 = Label(text = "Отрезок интегрирования [a, b]", font = "Arial 14")
label3 = Label(text = "δ = ", font = "Arial 14")
label4 = Label(text = "a = ", font = "Arial 14")
label5 = Label(text = "b = ", font = "Arial 14")
label6 = Label(text = "Шаг ", font = "Arial 14")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
label4.grid(row=3, column=0)
label5.grid(row=4, column=0)
label6.grid(row=5, column=0)

combo = Combobox(root)  
combo['values'] = (0.1, 0.01, 0.001)  
combo.current(1)  # установите вариант по умолчанию  
combo.grid(row=5, column=1)  

_a=DoubleVar()
_b=DoubleVar()
_c=DoubleVar()

entry1 = Entry(textvariable = _c, font = "Arial 14")
entry2 = Entry(textvariable = _a, font = "Arial 14")
entry3 = Entry(textvariable = _b, font = "Arial 14")

a = 0.0
b = 0.0
c = 0.0
h = 0.0

x_ = 0.0
y_ = 0.0
count = 0

entry1.delete(0, END)
entry1.insert(0, "1")

entry1.grid(row=2, column=1, padx=5, pady=5)
entry2.grid(row=3, column=1, padx=5, pady=5)
entry3.grid(row=4, column=1, padx=5, pady=5)


btn = Button(text= "Задать начальные условия", font = "Arial 14", command =lambda: entry(float(_a.get()), float(_b.get()), float(_c.get()), float(combo.get())))
btn.grid(row=6,column=1)

root.mainloop() # запускает цикл обработки событий окна
