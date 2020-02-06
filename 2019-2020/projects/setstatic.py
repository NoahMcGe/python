import os
import socket
bash=os.system
myhost = os.uname()[1]

def ip():
	global m
	m="ifconfig wlan0 192.168.7."+myhost+" netmask 255.255.255.0"
	print(m)
def resolv():
	global m2
	global m3
	global m4
	global m5
	m2="rm -f /etc/resolv.conf"
	m3="touch /etc/resolv.conf"
	m4="echo nameserver 192.168.7.1 >> /etc/rosolv.conf"
	m5="--------------------------------"
	print(m2)
	print(m3)
	print(m4)
	print(m5)
def execute():
	a = input ("Does everything above look correct? (Y/N): ")
	if (a == "Y" or a == "y"):
		a = input ("Would you like to execute the commands? (Y/N): ")
		if (a == "Y" or a == "y"):
			bash(m)
			bash(m2)
			bash(m3)
			bash(m4)
		elif (a == "N" or a == "n"):
			print(m5)
			print("Exiting ip script no changes made.")
			exit()
		else:
			execute()
	elif (a == "N" or a == "n"):
		print(m5)
		print("Make sure your hostname is changed to the ip you wish...\nExiting ip script no changes made.")
		exit()
	else:
		execute()
def main():
	ip()
	resolv()
	execute()
if __name__ == "__main__":
    main()

