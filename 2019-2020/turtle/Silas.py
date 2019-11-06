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
l = turtle.Turtle()
z = turtle.Turtle()
image = "img/x.gif"
move_speed = 10
turn_speed = 10

def logo():
    w.addshape(image)
    z.shape(image)
    z.penup()
    z.speed(0)
    x=-100
    y=100
    z.goto(x,y)


def forward():
  z.forward(move_speed)

def backward():
  z.backward(move_speed)

def left():
  z.left(turn_speed)

def right():
  z.right(turn_speed)


def go():
	Ness(80,10)

def Ness(len1,len2): #shape1 and shape 2 should be last, and add a nat 20 dice for cool spell
    l.speed(10)
    l.penup()
    l.setheading(0)
    l.pendown()
    l.color("#ffffff")
    l.fillcolor("#cc3939")
    for x in range(1):
        l.penup()
        l.goto(200,200)
        l.pendown()
        l.begin_fill()
        l.width(2)
        l.fd(len1)
        l.left(90)
        l.fd(len2)
        l.right(90)
        l.fd(len2)
        l.left(90)
        l.fd(len1)
        l.left(90)
        l.fd(len2)
        l.right(90)
        l.fd(len2)
        l.left(90)
        l.fd(len1)
        l.left(90)
        l.fd(len2)
        l.right(90)
        l.fd(len2)
        l.left(90)
        l.fd(len1)
        l.left(90)
        l.fd(len2)
        l.right(90)
        l.fd(len2)
        l.end_fill()
        l.left(90)
        l.penup()
        l.pensize(5)
        l.fd(10)
        l.left(90)
        l.fd(20)
        l.right(45)
        l.pendown()
        l.fd(85)
        l.left(90 + 45)
        l.penup()
        l.fd(60)
        l.left(90 + 45)
        l.pendown()
        l.fd(85)
        l.penup()
        l.left(45)
        l.fd(200)



def failed():
	xpo = ccx  - 35
	ypo = ccy + 150
	need.text(xpo + 240, ypo - 320, "Task Failed Successfully", black, 18)

def xp():
	xpo = ccx  - 85
	ypo = ccy + 210
	need.text(xpo + 200, ypo - 200, "Windows XP", white, 20)
	
def ok():
	xpo = ccx  + 115
	ypo = ccy - 145
	need.text(xpo + 200, ypo - 200, "OK", black, 24)


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
	t.forward(480) #First movement, in the x axis
	t.rt(90)
	t.forward(460) # second movement, in the -y axis
	t.rt(90)
	t.forward(480) # Third movement in the -x axis
	t.rt(90)
	t.forward(460) # fourth movement in the y axis
	t.end_fill()

def square2():
	xpo = ccx  + 105
	ypo = ccy - 5
#Start of second square
	r.penup()
	r.goto(xpo,ypo)
	r.pendown()
	r.begin_fill()
	#tcolor = "#fff9ed"
	rcolor = "#fff2d1"
	r.color(rcolor)
	r.forward(470) #First movement, in the x axis
	r.rt(90)
	r.forward(400) # second movement, in the -y axis
	r.rt(90)
	r.forward(470) # Third movement in the -x axis
	r.rt(90)
	r.forward(400) # fourth movement in the y axis
	r.end_fill()

def square3():
	xpo = ccx  + 270
	ypo = ccy - 350
	#Start of second square
	r.penup()
	r.goto(xpo,ypo)
	r.pendown()
	#r.begin_fill()
	#tcolor = "#fff9ed"
	rcolor = "#000000"
	r.color(rcolor)
	r.forward(50) #First movement, in the x axis
	r.rt(90)
	r.forward(150) # second movement, in the -y axis
	r.rt(90)
	r.forward(50) # Third movement in the -x axis
	r.rt(90)
	r.forward(150) # fourth movement in the y axis
	#r.end_fill()

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
root.minsize(350, 100)
d = tk.Button(root, text="failed",font=('courier', '20') ,command=failed)
c = tk.Button(root, text="xp",font=('courier', '20') ,command=xp)
b = tk.Button(root, text="st",font=('courier', '20') ,command=st)
e = tk.Button(root, text="st2",font=('courier', '20') ,command=square2)
f = tk.Button(root, text="st3",font=('courier', '20') ,command=square3)
a = tk.Button(root, text="ok",font=('courier', '20') ,command=ok)
g = tk.Button(root, text="X",font=('courier', '20') ,command=go)
h = tk.Button(root, text="logo",font=('courier', '20') ,command=logo)
#d = tk.Button(root, text="CLEAR + loltyler1.com discountcode:ALPHA",font=('courier', '20') ,command=end)
#y = tk.Button(root, text="CLEAR + Cool Boy",font=('courier', '20') ,command=loop2)
t1 = tk.Label(root, text="-Noah McGe",font=('courier', '10'))
b.pack()
e.pack()
f.pack()
h.pack()
c.pack()
a.pack()
d.pack()
g.pack()
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
