# Noah McGehee
# Changes the name from Steve-pi in minecraftpyed on an RPI
# Needs to be in the same folder as the minecraft-pi when you run the script

import re
import os
import sys
bash=os.system
clean = []
b = ""
a = ""


def piname():
	global a
	a = input ("Type in your name, it has to be 7 characters long, no more no less! : ")
	if len(a) != 7 :
		print ("Error! Name must be 7 characters!")
		print ("---------------------------------------------")
		a = ""
		piname()
	main()

def main():
	global clean
	global a
	global b
	n = len(a)

	for i in range(0, n):
			clean = hex(ord(a[i]))[2:4]
			#print(clean,end='')
			b += clean
	print("")
	print(str(b))
	print ("---------------------------------------------")
	m="hexdump -ve \'1/1 \"%.2X\"\' minecraft-pi > mcpi.txt;"
	m2='sed -i ''"s/53746576655069/'+ str(b) +'/g" mcpi.txt;'
	m3="xxd -r -p mcpi.txt > minecraft-pi;"
	m4="chown pi:pi minecraft-pi;"
	m5="chmod a+x minecraft-pi;"
	print(m + "\n" + m2 + "\n" + m3 + "\n" + m4 + "\n" + m5)
	bash(m+m2+m3+m4+m5)
	exit()

if __name__ == "__main__":
	piname()
	main()
