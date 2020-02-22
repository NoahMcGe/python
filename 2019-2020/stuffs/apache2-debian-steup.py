import os
import socket
import getpass
bash=os.system
username = getpass.getuser()
myhost = os.uname()[1]
line1="----------------------------------"

def apache2set():
	print("Username:"+username+" Hostname:"+myhost)
	print(line1)
	print("WARNING : YOU MUST NOT RUN THIS AS ROOT")
	print("YOU MUST BE A MEMBER OF THE SUDO GROUP TO RUN THIS")
	print(line1)
	a = input ("Would you like to run the apache setup file? Y/N : ")
	if (a == "Y" or a == "y"):
		bash("sudo apt install apache2")
		bash("cd /home/"+username+"/;mkdir http/;cd http/;mkdir logs;cd ..;chmod 755 http/ -R")#makes http and logs folder and changes perms
		bash("wget https://raw.githubusercontent.com/NoahMcGe/documents/master/apache/localhost.conf;chmod 755 localhost.conf;")#downloads debian apache2 localhost.conf file and changes perms
		#bash("sed -i 's/ifb/"+username+"/g' localhost.conf;cd /etc/apache2/sites-available/;sudo rm /etc/apache2/sites-available/*.conf;cd ../sites-enabled/;sudo rm /etc/apache2/sites-enabled/*.conf")#changing the username to match the end user, removing files
		#sed -i 's/original/new/g' file.txt #example of sed command in case changes need to be made
		#bash("sudo mv localhost.conf /etc/apache2/sites-available/;cd /etc/apache2/sites-available/;sudo a2ensite localhost.conf;")# moving the localhost file
		#bash("sudo systemctl reload apache2")
		#php()
	elif (a == "N" or a == "n"):
		print("Did not try to setup apache")
		exit()
	else:
		apache2set()

def php():
	a = input ("Would you like to install the newest version of PHP and the dependencies? Y/N : ")
	if (a == "Y" or a == "y"):
		print("Installing PHP")
		bash("sudo apt install php -y")
		exit()
	elif (a == "N" or a == "n"):
		print("Did not try to install php")
	else:
		php()
def main():
	apache2set()

if __name__ == "__main__":
    main()
