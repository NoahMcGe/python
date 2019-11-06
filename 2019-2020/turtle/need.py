#pn code

import tkinter as tk
import turtle

def penupsetxy(xcord, ycord):
	turtle.penup()
	turtle.setx(xcord)
	turtle.sety(ycord)
	turtle.pendown()

def rectangle_outline(x, y, width, height, color):#this is really poop, but its the first thing i made so of-course it is dumby
	turtle.color(color)
	penupsetxy(x, y)
	turtle.forward(width)
	penupsetxy(x, y)
	turtle.right(90)
	turtle.forward(height)
	penupsetxy(x + width, y)
	turtle.forward(height)
	penupsetxy(x, y - height)
	turtle.left(90)
	turtle.forward(width)
	
def rectangle_filled(x, y, width, height, color):
	turtle.fillcolor(color)
	penupsetxy(x, y)
	turtle.begin_fill()
	for _ in range(2):#not my part, but is nice
		turtle.forward(width)
		turtle.right(90)
		turtle.forward(height)
		turtle.right(90)
	turtle.end_fill()

def line_wide(x, y, width, color):
	turtle.color(color)
	penupsetxy(x, y)
	turtle.forward(width)
	
def line_long(x, y, height, color):
	turtle.color(color)
	penupsetxy(x, y)
	turtle.right(90)
	turtle.forward(height)
	
def text(x, y, inputtxt, color, font_size):
	style = ('Tahoma', font_size, 'bold')
	turtle.color(color)
	penupsetxy(x, y)
	turtle.write(inputtxt, font=style)
