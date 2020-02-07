import os
import socket
import getpass
bash=os.system
username = getpass.getuser()
myhost = os.uname()[1]

def apache2set():
	print("Username:"+username+" Hostname:"+myhost)
	bash("sudo apt install apache2")
	bash("cd /home/"+username+"/;mkdir http/;cd http/;mkdir logs;cd ..;chmod 755 http/ -R;")#makes http and logs folder and changes perms
  	bash("wget https://raw.githubusercontent.com/NoahMcGe/documents/master/apache/localhost.conf;chmod 755 localhost.conf;")#downloads debian apache2 localhost.conf file and changes perms
	bash("sed -i 's/ifb/"+username+"/g' localhost.conf;cd /etc/apache2/sites-available; rm *.conf;cd ../sites-enabled/;rm *.conf")#changing the username to match the end user, removing files
	#sed -i 's/original/new/g' file.txt #example of sed command in case changes need to be made
	bash("mv localhost.conf /etc/apache2/sites-avalible;cd /etc/apache2/sites-available/;a2ensite localhost.conf;systemctl reload apache2;")# moving the localhost file and reloading apache

def php():
	a = input ("Would you like to install the newest version of php? Y/N")
	if (a == "Y" or a == "y"):
		Print("Installing the php")
		bash("sudo apt install php")
def main():
	apache2set()
