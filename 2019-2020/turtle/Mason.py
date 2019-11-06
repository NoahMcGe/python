#turtle_project.py mka
import turtle
import Tkinter as tk

t = turtle.Turtle()
ts = turtle.Screen()
ts.bgcolor("#123123")
t.width(10)

#Turtle Start

def go():
	Ness(80,10)

def Ness(len1,len2): #shape1 and shape 2 should be last, and add a nat 20 dice for cool spell
    ts.clear()
    t = turtle.Turtle()
    ts.bgcolor("#123123")
    t.speed(10)
    t.penup()
    t.setheading(0)
    t.pendown()
    t.color("#ffffff")
    t.fillcolor("#cc3939")
    for x in range(1):
        t.begin_fill()
        t.width(2)
        t.fd(len1)
        t.left(90)
        t.fd(len2)
        t.right(90)
        t.fd(len2)
        t.left(90)
        t.fd(len1)
        t.left(90)
        t.fd(len2)
        t.right(90)
        t.fd(len2)
        t.left(90)
        t.fd(len1)
        t.left(90)
        t.fd(len2)
        t.right(90)
        t.fd(len2)
        t.left(90)
        t.fd(len1)
        t.left(90)
        t.fd(len2)
        t.right(90)
        t.fd(len2)
        t.end_fill()
        t.left(90)
        t.penup()
        t.pensize(5)
        t.fd(10)
        t.left(90)
        t.fd(20)
        t.right(45)
        t.pendown()
        t.fd(85)
        t.left(90 + 45)
        t.penup()
        t.fd(60)
        t.left(90 + 45)
        t.pendown()
        t.fd(85)
        t.penup()
        t.left(45)
        t.fd(200)
   
root = tk.Tk()
root.option_add("*Font", "courier")
root.wm_title("GUI")
root.minsize(400, 200)
a = tk.Button(root, text="Something",font=('courier', '20') ,command=go)
t1 = tk.Label(root, text="Something Else",font=('courier', '10'))
a.pack()
t1.pack()
root.mainloop()



#Ness(80,10)


holdit = input();
