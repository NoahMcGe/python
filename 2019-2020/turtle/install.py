import os
import random
os.system("date")

def art():
	i = random.randrange(13) + 1
	website="http://10.183.1.19/git/noah/python/2019-2020/turtle/art/"+ str(i) + ".txt"
	#website="https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
	os.system("curl " +  website)

def run():
	a = input ("Would you like to download the group python project? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("wget http://10.183.1.19/git/noah/python/2019-2020/turtle/run.py")
		os.system("mkdir py")
		os.system("cd py/;wget http://10.183.1.19/git/noah/python/2019-2020/turtle/py/group.py;wget http://10.183.1.19/git/noah/python/2019-2020/turtle/py/need.py")
		os.system("mkdir img")
		os.system("cd img/;wget http://10.183.1.19/git/noah/python/2019-2020/turtle/img/42.png;wget http://10.183.1.19/git/noah/python/2019-2020/turtle/img/x.gif")
		os.system("date")
	elif (a == "N" or a == "n"):
		exit()
	else:
		run()

def run2():
	a = input ("Would you like to run the group python project? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("python3 py/group.py")
	elif (a == "N" or a == "n"):
		exit()
	else:
		run()
run()
art()
run2()

