#ty 2 pn for help wit text

import tkinter as tk
import turtle

def penupsetxy(xcord, ycord):
	turtle.penup()
	turtle.setx(xcord)
	turtle.sety(ycord)
	turtle.pendown()


def text(x, y, inputtxt, color, font_size):
	style = ('Tahoma', font_size, 'bold')
	turtle.color(color)
	penupsetxy(x, y)
	turtle.write(inputtxt, font=style)
