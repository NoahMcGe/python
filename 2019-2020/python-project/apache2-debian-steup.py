import os
import socket
import getpass
bash=os.system
username = getpass.getuser()
myhost = os.uname()[1]

def apache2set():
	print("Username:"+username+" Hostname:"+myhost)
	bash("cd /home/"+username+"/;mkdir http/;cd http/;mkdir logs;cd ..;chmod 755 http/ -R;")
  bash("wget https://raw.githubusercontent.com/NoahMcGe/documents/master/apache/localhost.conf;chmod 755 localhost.conf;")
#sed -i 's/original/new/g' file.txt
def main():
	apache2set()
