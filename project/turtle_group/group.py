#ex4.py nm ts j

import tkinter as tk

from random import randint

import colorsys

import turtle  #Inside_Out

from turtle import *

#All of our imports
#--------------------------------------------------------------------------
#noah's turtle and setup
for i in range(10):
	color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
w = turtle.Screen()
w.bgpic("img/egg.gif")
q = turtle.Turtle()

def start():
	for i in range(570):
		print(i)
		color = colorsys.hsv_to_rgb(i/700, 1.0, 1.0)
		q.pencolor(color)
		q.backward(i)
		q.right(126)
		q.speed(0)
		q.width(5)
#--------------------------------------------------------------------------
#tyler's turtles
r = turtle.Turtle()
def start2():
	for i in range(190):
		print(i)
		color = colorsys.hsv_to_rgb(i/170, 0.8, 1.0)
		r.pencolor(color)
		r.backward(i)
		r.right(25)
		r.speed(0)
		r.width(4)

#--------------------------------------------------------------------------
p = turtle.Turtle()
def start3():
	for i in range(210):
		print(i)
		color = colorsys.hsv_to_rgb(i/100, 1.0, 1.0)
		p.pencolor(color)
		p.backward(i)
		p.right(72)
		p.speed(0)

#--------------------------------------------------------------------------

#end clearscreen
def end():
	turtle.Screen().clear()
	w.bgpic("img/egg.gif")
	
def end2():
	turtle.Screen().clear()
	w.bgpic("img/ole-the-one-punch-man-dub-is-still-good-4560098.png")
	
def end3():
	turtle.Screen().clear()
	w.bgpic("img/ggx.gif")

def loop():
	turtle.Screen().clear()
	w.bgpic("img/tyler1__the_alpha_male__freetyler1_by_idcfrost-dbjv5bz.png")
	
def loop2():
	turtle.Screen().clear()
	w.bgpic("img/32.gif")

def loop3():
	turtle.Screen().clear()
	w.bgpic("img/C000000568-PAR-ZOOM_85c9f42d-aa83-42f6-b42f-4bfe73b1dfd4_800x.png")
	

#--------------------------------------------------------------------------
#menu , ty Mr.Coleman
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("MENU - Noah, Tyler, Jorge! OUR PYTHON PRESENTATION")
root.minsize(500, 400)
a = tk.Button(root, text="Noah",font=('courier', '20') ,command=start)
b = tk.Button(root, text="Tyler",font=('courier', '20') ,command=start2)
c = tk.Button(root, text="Jorge",font=('courier', '20') ,command=start3)
d = tk.Button(root, text="CLEAR + loltyler1.com discountcode:ALPHA",font=('courier', '20') ,command=end)
e = tk.Button(root, text="CLEAR + OnePunch!",font=('courier', '20') ,command=end2)
f = tk.Button(root, text="CLEAR + GGX Gang",font=('courier', '20') ,command=end3)
z = tk.Button(root, text="CLEAR + (SSJ)Alpha Male",font=('courier', '20') ,command=loop)
y = tk.Button(root, text="CLEAR + Cool Boy",font=('courier', '20') ,command=loop2)
i = tk.Button(root, text="CLEAR + LOST",font=('courier', '20') ,command=loop3)
t1 = tk.Label(root, text="*Modern Art* (Colorful spinner on tyler1) : Noah McGehee",font=('courier', '10'))
t2 = tk.Label(root, text="*Black Hole* (A crazy spin on an old trick! colorful) : Tyler",font=('courier', '10'))
t3 = tk.Label(root, text = "Its Colorful its new! its BLUE! (Brought to you by jorge!)",font=('courier', '10'))
a.pack()
b.pack()
c.pack()
d.pack()
e.pack()
f.pack()
z.pack()
y.pack()
i.pack()
t1.pack()
t2.pack()
t3.pack()
root.mainloop()
#--------------------------------------------------------------------------
