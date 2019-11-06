#Noah McGe
import tkinter as tk
from random import randint
import colorsys
import turtle 
from turtle import *
import need
#--------------------------------------------------------------------------
#noah's turtle and setup
for i in range(10):
	color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
w = turtle.Screen()
turtle.setup(500,500)
w.bgpic("img/egg.gif")
q = turtle.Turtle()
ccx = -300
ccy = 250
black = "#000000"
white = "#ffffff"
def failed():
	xpo = ccx  + 5
	ypo = ccy - 5
	need.text(xpo + 240, ypo - 320, "Task Failed Successfully", black, 11)
	
def xp():
	xpo = ccx  + 5
	ypo = ccy - 5
	need.text(xpo + 200, ypo - 200, "Windows XP", white, 16)

def start():
	for i in range(570):
		print(i)
		color = colorsys.hsv_to_rgb(i/700, 1.0, 1.0)
		q.pencolor(color)
		q.backward(i*1.7)
		q.right(126)
		q.speed(0)
		q.width(9)

#--------------------------------------------------------------------------

#end clearscreen
def end():
	turtle.Screen().clear()
	w.bgpic("img/egg.gif")
	
def loop2():
	turtle.Screen().clear()
	w.bgpic("img/32.gif")
	

#--------------------------------------------------------------------------
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("Noah's Menu")
root.minsize(300, 100)
b = tk.Button(root, text="failed",font=('courier', '20') ,command=failed)
c = tk.Button(root, text="xp",font=('courier', '20') ,command=xp)
a = tk.Button(root, text="Noah",font=('courier', '20') ,command=start)
d = tk.Button(root, text="CLEAR + loltyler1.com discountcode:ALPHA",font=('courier', '20') ,command=end)
y = tk.Button(root, text="CLEAR + Cool Boy",font=('courier', '20') ,command=loop2)
t1 = tk.Label(root, text="-Noah McGe",font=('courier', '10'))
b.pack()
c.pack()
a.pack()
d.pack()
#e.pack()
#f.pack()
#z.pack()
y.pack()
#i.pack()
t1.pack()
#t2.pack()
#t3.pack()
root.mainloop()
#--------------------------------------------------------------------------
