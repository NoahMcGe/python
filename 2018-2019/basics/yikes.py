import colorsys
import turtle
turtle.bgpic("turtle/img/egg.gif")
t = turtle.Turtle()
f = turtle.Turtle()

for i in range(200):
	print(i)
	color = colorsys.hsv_to_rgb(i/700, 1.0, 1.0)
	t.pencolor(color)
	t.backward(i)
	t.right(126)
	t.speed(0)
for i in range(1000):
	print(i)
	color = colorsys.hsv_to_rgb(i/1000, 1.0, 1.0)
	f.pencolor(color)
	f.forward(i)
	f.right(98)
	f.speed(0)
holdit = input();

'''
https://docs.python.org/2/library/colorsys.html

'''
