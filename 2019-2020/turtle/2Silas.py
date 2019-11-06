import turtle
import tkinter as tk
from random import randint
import colorsys
from turtle import *
import need
q = turtle.Turtle()
for i in range(10):
	color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
ccx = -300
ccy = 250
black = "#000000"
white = "#ffffff"
w = turtle.Screen()
w.setup(1000, 700)
w.clear()
w.bgpic("img/42.png")
q = turtle.Turtle()
r = turtle.Turtle()
t = turtle.Turtle()


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

def square(t,x,y):
	t.penup()
	t.goto(x,y)
	t.pendown()
	t.begin_fill()
	#tcolor = "#fff9ed"
	tcolor = "#0000ff"
	t.color(tcolor)
	t.forward(430) #First movement, in the x axis
	t.rt(90)
	t.forward(500) # second movement, in the -y axis
	t.rt(90)
	t.forward(430) # Third movement in the -x axis
	t.rt(90)
	t.forward(500) # fourth movement in the y axis
	t.end_fill()

def square2():
	xpo = ccx  + 100
	ypo = ccy - 5
#Start of second square
	r.penup()
	r.goto(xpo,ypo)
	r.pendown()
	r.begin_fill()
	#tcolor = "#fff9ed"
	rcolor = "#fff2d1"
	r.color(rcolor)
	r.forward(430) #First movement, in the x axis
	r.rt(90)
	r.forward(300) # second movement, in the -y axis
	r.rt(90)
	r.forward(430) # Third movement in the -x axis
	r.rt(90)
	r.forward(500) # fourth movement in the y axis
	r.end_fill()

def st():
	#t.penup()
	x = -200; y = 300
	t.penup()
	t.goto(-200,0)
	t.speed(5)
	t.color("#000000")
	#t.forward(10)
	#Start of second square
	t.penup()
	#x = -190; y = -200
	t.goto(-190,-200)
	#t.forward(10)
	t.pendown()
	#t.pendown()
	square(t,x,y)
    #circle(t)
	#w.exitonclick()

'''if __name__ == '__main__':
	main()
	#main2()
	holdit = input();
'''
	
	
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("Noah's Menu")
root.minsize(300, 100)
d = tk.Button(root, text="failed",font=('courier', '20') ,command=failed)
c = tk.Button(root, text="xp",font=('courier', '20') ,command=xp)
b = tk.Button(root, text="st",font=('courier', '20') ,command=st)
e = tk.Button(root, text="st2",font=('courier', '20') ,command=square2)
a = tk.Button(root, text="Noah",font=('courier', '20') ,command=start)
#d = tk.Button(root, text="CLEAR + loltyler1.com discountcode:ALPHA",font=('courier', '20') ,command=end)
#y = tk.Button(root, text="CLEAR + Cool Boy",font=('courier', '20') ,command=loop2)
t1 = tk.Label(root, text="-Noah McGe",font=('courier', '10'))
b.pack()
c.pack()
a.pack()
d.pack()
e.pack()
#f.pack()
#z.pack()
#y.pack()
#i.pack()
t1.pack()
#t2.pack()
#t3.pack()
root.mainloop()
#--------------------------------------------------------------------------
'''
#apt install python3-tk



wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
