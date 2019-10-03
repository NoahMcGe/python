#ex4.py nm
import colorsys
for i in range(10):
	color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
import turtle  #Inside_Out
from turtle import *
w = turtle.Screen()
w.bgpic("img/egg.gif")
q = turtle.Turtle()
t = turtle.Turtle()
t.color("white")
t.width(5)
t.speed(5)
f = turtle.Turtle()
f.color("#E71010")
f.width(5)
f.speed(5)
y = turtle.Turtle()
y.color("purple")
y.width(5)
y.speed(5)
z = turtle.Turtle()
z.color("#FF8F8F")
z.width(5)
z.speed(5)
p = turtle.Turtle()
p.color("#FFED00")
p.width(5.8)
p.speed(5)

for i in range(570):
	print(i)
	color = colorsys.hsv_to_rgb(i/700, 1.0, 1.0)
	q.pencolor(color)
	q.backward(i)
	q.right(126)
	q.speed(0)


def oof(size):
	for i in range(36):
		t.fd(size)
		t.left(75)
		size = size + 11
		
def foo(size):
	for i in range(36):
		f.fd(size)
		f.left(75)
		size = size + 11.2
		
def yikes(size):
	for i in range(36):
		y.fd(size)
		y.left(75)
		size = size + 11.4
		
def yikes2(size):
	for i in range(36):
		z.fd(size)
		z.left(75)
		size = size + 11.6
		
def poof(size):
	for i in range(36):
		p.fd(size)
		p.left(75)
		size = size + 11.8



oof(6)
foo(7)
yikes(8)
yikes2(9)
poof(10)


holdit = input();
