import tkinter as tk

from random import randint

import colorsys

import turtle  #Inside_Out

from turtle import *


for i in range(10):
	color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)

p = turtle.Turtle()

def start():
	for i in range(190):
		print(i)
		color = colorsys.hsv_to_rgb(i/170, 0.8, 1.0)
		r.pencolor(color)
		r.backward(i)
		r.right(25)
		r.speed(0)
		r.width(4)

root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("MENU - Noah, Tyler, Jorge! OUR PYTHON PRESENTATION")
root.minsize(100, 50)
a = tk.Button(root, text="Start",font=('courier', '20') ,command=start)


a.pack()


root.mainloop()
