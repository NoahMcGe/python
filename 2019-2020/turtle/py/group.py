#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  ___      _             
 / __| ___| |_ _  _ _ __ 
 \__ \/ -_)  _| || | '_ \
 |___/\___|\__|\_,_| .__/
                   |_|   
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

import turtle
import tkinter as tk
from random import randint
import random
import os
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


#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  ___ ___    ___ ___  _  _ ___ ___ _____ ___ ___  _  _ 
 |_ _| __|  / __/ _ \| \| |   \_ _|_   _|_ _/ _ \| \| |
  | || _|  | (_| (_) | .` | |) | |  | |  | | (_) | .` |
 |___|_|    \___\___/|_|\_|___/___| |_| |___\___/|_|\_|
                                                       
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def lolololol():
    if 1 > 0 :
	    l.penup()
	    q.penup()
	    r.penup()
	    t.penup()
	    l.goto(1000,1000)
	    q.goto(1000,1000)
	    r.goto(1000,1000)
	    t.goto(1000,1000)
    else:
	    print("The Heck how is 1 not > 0")

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  _                      __  ___ _    _                
 | |   ___  __ _ ___    / / | _ (_)__| |_ _  _ _ _ ___ 
 | |__/ _ \/ _` / _ \  / /  |  _/ / _|  _| || | '_/ -_)
 |____\___/\__, \___/ /_/   |_| |_\__|\__|\_,_|_| \___|
           |___/                                       
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def logo():
    w.addshape(image)
    z.shape(image)
    z.penup()
    z.speed(0)
    x=-120
    y=100
    z.goto(x,y)

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
 __  __   ___      _   _            
 \ \/ /__| _ )_  _| |_| |_ ___ _ _  
  >  <___| _ \ || |  _|  _/ _ \ ' \ 
 /_/\_\  |___/\_,_|\__|\__\___/_||_|
                                    
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def go():
	Ness(40,5)

def Ness(len1,len2): #shape1 and shape 2 should be last, and add a nat 20 dice for cool spell
    l.speed(10)
    l.penup()
    l.setheading(0)
    l.pendown()
    l.color("#ffffff")
    l.fillcolor("#cc3939")
    for x in range(1):
        l.penup()
        l.goto(225,247)
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
        l.pensize(3)
        l.fd(5)
        l.left(90)
        l.fd(10)
        l.right(45)
        l.pendown()
        l.fd(42)
        l.left(90 + 45)
        l.penup()
        l.fd(30)
        l.left(90 + 45)
        l.pendown()
        l.fd(42)
        l.penup()
        l.left(45)
        l.fd(200)

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  ___     _ _        _   _____        _   
 | __|_ _(_) |___ __| | |_   _|____ _| |_ 
 | _/ _` | | / -_) _` |   | |/ -_) \ /  _|
 |_|\__,_|_|_\___\__,_|   |_|\___/_\_\\__|
                                          
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def failed():
	xpo = ccx  - 35
	ypo = ccy + 150
	need.text(xpo + 285, ypo - 320, "Task Failed Successfully", black, 18)
	
#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
 __      ___         _                __  _____   _____        _   
 \ \    / (_)_ _  __| |_____ __ _____ \ \/ / _ \ |_   _|____ _| |_ 
  \ \/\/ /| | ' \/ _` / _ \ V  V (_-<  >  <|  _/   | |/ -_) \ /  _|
   \_/\_/ |_|_||_\__,_\___/\_/\_//__/ /_/\_\_|     |_|\___/_\_\\__|
                                                                   
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def xp():
	xpo = ccx  - 85
	ypo = ccy + 210
	need.text(xpo + 200, ypo - 200, "Windows XP", white, 20)
	
#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
   ___  _  __  _____        _   
  / _ \| |/ / |_   _|____ _| |_ 
 | (_) | ' <    | |/ -_) \ /  _|
  \___/|_|\_\   |_|\___/_\_\\__|
                                
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------
	
def ok():
	xpo = ccx  + 115
	ypo = ccy - 145
	need.text(xpo + 200, ypo - 200, "OK", black, 24)

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  _                  
 | |   ___  ___ _ __ 
 | |__/ _ \/ _ \ '_ \
 |____\___/\___/ .__/
               |_|   
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def start():
	for i in range(570):
		print(i)
		color = colorsys.hsv_to_rgb(i/700, 1.0, 1.0)
		q.pencolor(color)
		q.backward(i*1.7)
		q.right(190)
		q.speed(0)
		if i < 30:
			q.width(3)
		if 30 < i < 100:
			q.width(5)
		if 100 < i < 200:
			q.width(7)
		if 200 < i < 300:
			q.width(10)
		if 300 < i < 400:
			q.width(13)
		if 400 < i < 500:
			q.width(15)
		if 500 < i < 600:
			q.width(18)


#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  _  _     _     ___      _             _   _            _ 
 | \| |___| |_  | _ ) ___(_)_ _  __ _  | | | |___ ___ __| |
 | .` / _ \  _| | _ \/ -_) | ' \/ _` | | |_| (_-</ -_) _` |
 |_|\_\___/\__| |___/\___|_|_||_\__, |  \___//__/\___\__,_|
                                |___/                      
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

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

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  _____            ___          
 |_   _|_ _ _ _   | _ ) _____ __
   | |/ _` | ' \  | _ \/ _ \ \ /
   |_|\__,_|_||_| |___/\___/_\_\
                                
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def square2():
	xpo = ccx  + 105
	ypo = ccy - 5
#Start of second square
	r.penup()
	r.goto(xpo,ypo)
	r.speed(8)
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

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
   ___  _     ___          
  / _ \| |__ | _ ) _____ __
 | (_) | / / | _ \/ _ \ \ /
  \___/|_\_\ |___/\___/_\_\
                           
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

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
	r.pensize(3)
	r.forward(50) #First movement, in the x axis
	r.rt(90)
	r.forward(150) # second movement, in the -y axis
	r.rt(90)
	r.forward(50) # Third movement in the -x axis
	r.rt(90)
	r.forward(150) # fourth movement in the y axis
	#r.end_fill()
	
#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  ___ _            ___          
 | _ ) |_  _ ___  | _ ) _____ __
 | _ \ | || / -_) | _ \/ _ \ \ /
 |___/_|\_,_\___| |___/\___/_\_\
                                
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def st():
	#t.penup()
	x = -200; y = 300
	t.penup()
	t.goto(-200,0)
	t.speed(8)
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

#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
    ___         __ 
   /   |  _____/ /_
  / /| | / ___/ __/
 / ___ |/ /  / /_  
/_/  |_/_/   \__/  
                   
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------

def art():
	i = random.randrange(15) + 1
	website="https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/art/"+ str(i) + ".txt"
	#website="https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt" ty DanCRichards!!!!
	os.system("curl " +  website)



#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  __  __                 __  __              
 |  \/  |___ _ __  ___  |  \/  |___ _ _ _  _ 
 | |\/| / -_) '  \/ -_) | |\/| / -_) ' \ || |
 |_|  |_\___|_|_|_\___| |_|  |_\___|_||_\_,_|
                                             
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("Meme Menu")
root.minsize(350, 100)
d = tk.Button(root, text="Text Failed",font=('courier', '20') ,command=failed)
c = tk.Button(root, text="Text XP",font=('courier', '20') ,command=xp)
b = tk.Button(root, text="Step 1",font=('courier', '20') ,command=st)
e = tk.Button(root, text="Step 2",font=('courier', '20') ,command=square2)
f = tk.Button(root, text="Step 3",font=('courier', '20') ,command=square3)
a = tk.Button(root, text="Text OK",font=('courier', '20') ,command=ok)
g = tk.Button(root, text="X Button",font=('courier', '20') ,command=go)
h = tk.Button(root, text="Add logo",font=('courier', '20') ,command=logo)
j = tk.Button(root, text="Loooop",font=('courier', '20') ,command=start)
i = tk.Button(root, text="Send Turtles boiys Home",font=('courier', '20') ,command=lolololol)
k = tk.Button(root, text="Art",font=('courier', '20') ,command=art)
#d = tk.Button(root, text="CLEAR + loltyler1.com discountcode:ALPHA",font=('courier', '20') ,command=end)
#y = tk.Button(root, text="CLEAR + Cool Boy",font=('courier', '20') ,command=loop2)
#e1 = tk.Entry(root, text="First Name")
t1 = tk.Label(root, text="-Noah, Mason, Silas",font=('courier', '10'))
b.pack()
e.pack()
f.pack()
h.pack()
c.pack()
a.pack()
d.pack()
g.pack()
i.pack()
j.pack()
k.pack()
#z.pack()
#y.pack()
#i.pack()
t1.pack()
#e1.pack()
#t2.pack()
#t3.pack()
root.mainloop()
#----------------------------------------------------------------------------------------------------------------------------------------------------
'''
  _  _              _            _    ___ 
 | || |_____ __ __ | |_ ___   __| |__|__ \
 | __ / _ \ V  V / |  _/ _ \ / _` / _ \/_/
 |_||_\___/\_/\_/   \__\___/ \__,_\___(_) 
                                          
'''
#----------------------------------------------------------------------------------------------------------------------------------------------------
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
