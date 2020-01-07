'''
Test this.
https://tritech-testsite.smapply.io/

Get the code: 10.183.1.26 code python
Plot circle data using python
- Change the background color
- Change the graph line colors
- Change the plot line color
- Change the plot dot color
- Label the graph with text Plotting Circumference and Diameter
- Label the axis with text (Circumference and Diameter)
- Upload to github with your name initials or name attached (plot-circle-list-cwc.py

'''
import os
import turtle
import math
wdth = 800; hgth = 800; bgstring = "#ffffff"
red = "#cc0000"; green = "#00cc00"; blue = "#0000cc"
os.system("mkdir img")
os.system("cd img/;wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/img/42.png")

def grid(t):
	x = -200; y = -200
	while (x < 250):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = -200; y = -200
	while (y < 250):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	t.penup()
	t.goto(150,300)
	t.pendown()
	t.color('#00ff00')
	style = ('Courier', 12, 'bold')
	t.goto(-200,300)
	t.write('Circle Circumference and Diameter Plot', font=style, align='left')
	t.penup()
	t.goto(-100,270)
	t.pendown()
	t.goto(-200,270)
	t.write('Noah McGehee', font=style, align='left')
	t.penup()
	t.goto(150,240)
	t.pendown()
	t.goto(-200,240)
	t.color(red)
	t.write('Red Line is not apart of the stats!', font=style, align='left')
	t.hideturtle()
	t.penup()

def plotCircles(t):
	x=1
	y=1
	pink="#FFC0CB"
	purple="#800080"
	d =  [-200+(x*11.1), -200+(x*12), -200+(x*11.7), -200+(x*11.5)] #x?
	c =  [-200+(x*38.85), -200+(x*42), -200+(x*39.78), -200+(x*39.1)] #y?
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(-200,-200)
	t.pendown()
	t.color(red)
	t.goto(dsorted[0]+50,csorted[0]+50)
	t.color(green)
	t.dot(5, green)
	t.goto(dsorted[1]+100,csorted[1]+100)
	t.color(blue)
	t.dot(5, blue)
	t.goto(dsorted[2]+150,csorted[2]+150)
	t.color(pink)
	t.dot(5, pink)
	t.color(purple)
	t.goto(dsorted[3]+200,csorted[3]+200)
	t.dot(5, purple)
	
def main():
	try:
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg=bgstring)
		print(turtle.Screen().screensize())
		w = turtle.Screen()
		w.bgpic("img/42.png")
		t = turtle.Turtle()
		t.hideturtle()
		t.speed(0)#Makes speed fast -noah
		grid(t)
		plotCircles(t)
		w.exitonclick()
	finally:
		turtle.Terminator()
	
if __name__ == '__main__':
	main()

'''
	# Using sorted + key 
	Output = sorted(Input, key = float) 
	# Using sorted + key 
	Output = sorted(Input, key = float) 
'''
