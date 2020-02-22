import os
os.system("date")

def install():
	print("This is to install all packages into a clean install of debian10; Please run this as sudo.")
	a = input ("Would you like to install all packages? (Y/N): ")
	if (a == "Y" or a == "y"):
		packages1()
		os.system("date")
	elif (a == "N" or a == "n"):
		print("Nothing to install")
		exit()
	else:
		install()
def packages1():
	os.system("apt install git neofetch net-tools php7.0 python3-tk apache python-serial curl sudo vlc filezilla flameshot -y")

install()
