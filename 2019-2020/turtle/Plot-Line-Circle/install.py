import os
import random
os.system("date")

def art():
	i = random.randrange(13) + 1
	website="https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/art/"+ str(i) + ".txt"
	#website="https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
	os.system("curl " +  website)

def run():
	print("All files will download where is the install file is located so please put it into a separate directory with no other files. ^-^")
	a = input ("Would you like to download the 42.png? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("mkdir img")
		os.system("cd img/;wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/Plot-Line-Circle/img/42.png")
		os.system("wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/Plot-Line-Circle/run.py")
		os.system("date")
	elif (a == "N" or a == "n"):
		run3()
		exit()
	else:
		run()

def run2():
	a = input ("Would you like to run Plot-Circle-Line? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("python3 run.py")
	elif (a == "N" or a == "n"):
		exit()
	else:
		run()
		
def run3():
	a = input ("Would you like to display the credits? (Y/N): ")
	if (a == "Y" or a == "y"):
		print("Maker and Baker - Noah")
		print("Chef BOI-R-dee - Preston")
	elif (a == "N" or a == "n"):
		print("did not display credits.")
	else:
		run3()

def run4():
	a = input ("Would you like to download instructions? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("wget https://raw.githubusercontent.com/NoahMcGe/python/master/2019-2020/turtle/Plot-Line-Circle/instructions.txt")
		run41()
	elif (a == "N" or a == "n"):
		print("did not download instructions.")
	else:
		run4()
		
def run41():
	a = input ("Would you like to read instructions? (Y/N): ")
	if (a == "Y" or a == "y"):
		os.system("cat instructions.txt")
	elif (a == "N" or a == "n"):
		print("did not display instructions.")
	else:
		run41()


run()
run4()
run3()
run2()
art()
os.system("rm install.py")
