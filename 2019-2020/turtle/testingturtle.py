import tkinter as tk
import turtle
import random
import need
#==========================#setup
_width = 600
_height = 450
posx = -300
posy = 250
turtle.bgcolor("#ff9933")
turtle.speed(50)
poob = turtle.Screen()
#==========================#colors
#menu_color = turtle.textinput("color", "input menu color:")
menu_color = "#1ecbcb"
light_gray = "#888888"
lighter_gray = "#707070"
dark_gray = "#505050"
black = "#000000"
white = "#999999"
darker_gray = "#202020"
darkish_gray = "#404040"
#==========================
def main():
	turtle.hideturtle()
	need.rectangle_outline(posx, posy, _width, _height, black)
	need.rectangle_outline(posx + 1, posy - 1, _width - 2, _height - 2, light_gray)
	need.rectangle_outline(posx + 2, posy - 2, _width - 4, _height - 4, dark_gray)
	need.rectangle_outline(posx + 3, posy - 3, _width - 6, _height - 6, dark_gray)
	need.rectangle_outline(posx + 4, posy - 4, _width - 8, _height - 8, light_gray)
	need.rectangle_outline(posx + 5, posy - 5, _width - 10, _height - 10, darker_gray)
	turtle.showturtle()#debug 
	#new things so i dont have to keep minusing by b1g numbers
	newheight = _height - 10
	newwidth = _width - 10
	newx = posx  + 5
	newy = posy - 5

	need.rectangle_filled(newx, newy, newwidth, newheight, darker_gray)
	need.line_wide(newx + 2, newy - 2, newwidth - 4, menu_color)#colorline
	
	need.rectangle_outline(newx + 12, newy - 16, newwidth - 24, 35, lighter_gray)
	need.rectangle_filled(newx + 12, newy - 16, newwidth - 24, 35, darkish_gray)
	need.text(newx + 40, newy - 43, "Legitbot", menu_color, 11)
	need.text(newx + 150, newy - 43, "Ragebot", white, 11)
	need.text(newx + 257, newy - 43, "Visuals", white, 11)
	need.text(newx + 347, newy - 43, "Miscellaneous", white, 11)
	need.text(newx + 492, newy - 43, "Config", white, 11)
	
	turtle.onclick(turtle.goto)

if __name__ == '__main__':
	main()

poob.exitonclick()
