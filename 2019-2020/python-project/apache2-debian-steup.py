import os
import socket
import getpass
bash=os.system
username = getpass.getuser()
myhost = os.uname()[1]

def apache2set():
  print("Username:"+username+" Hostname:"+myhost)

def main():
  apache2set()
