#dictionary.py NM
import tkinter as tk
import turtle

def main():
	#table is a dictionary
	table = {-100:1,-99:-10,-90:3,-89:-13,-80:5,-79:-15,-70:7,-69:-17,-60:9,-59:-19,-50:11,
				-49:-21,-40:13,-39:-23,-30:15,-29:-25,-20:17,-19:-27,-10:19,-9:-29,0:0,-1:-10,
					10:19,9:-29,20:17,19:-27,30:15,29:-25,40:13,39:-23,50:11,49:-21,
					60:9,59:-19,70:7,69:-17,80:5,79:-15,90:3,89:-13,100:1,99:-11,
			}
	print(" KEYS ")
	print(table.keys())
	print(" VALUES ")
	print(table.values())
	# turtle graphics
	twin = turtle.Screen()
	twin.clear()
	t = turtle.Turtle()
	#twin = turtle.Screen()
	for h,k in table.items(): #get the items in the dictionary
		print(h,k) # trace code 
		#x,y = table[n]
		t.penup()
		t.goto(h,k)
		t.pendown()
		t.circle(5)
		t.speed(20)
	twin.exitonclick()
	print("LETS GIT REEL U RNT A REAL GROWN MAN...LIKE THE REST OF US GET PUT OUT OF TOWN 4 I GIVE YOUR FACE A FROWN DONT MAKE ME THROW DOWN, STOP ACTING A CLOWN, THE KING JUZT RECIVED THIS CROWN AMAZON PRIME! I DIDNT PAY A DIME. ALL THESE RYMS IM DROPPIN LIKE SLIMES. APRENTLY YOU HADNT SEEN THAT I AM MEAN .FOR IF YOU HAD SEEN YOU WOULD NOT HAVE BEEN TURNED INTO A BEAN NEXT TIME DONT ACT AH MESS FOR I HIT YOU WIT THE NESS (SUPER SMASH BROTHERS)")
	
main()

