import os
import getpass
bash=os.system
username = getpass.getuser()
myhost = os.uname()[1]

def usernamepas():
    global a
    global b
    a = input("Username: ")
    b = input ("Password: ")

def testuserpass():
    if(a=="noah" or a=="Noah"):
        print("------------------------")
        if(b=="McGe"):
            bash('clear')
            bashfun()
        else:
            print("------------------------")
            print("Username Password Incorrect")
            main() 
    else:
        print("------------------------")
        print("Username Password Incorrect")
        main()

def bashfun():
    print('---------Path-------------------------------')
    bash("pwd")
    print('--------------------------------------------')
    c=input(username+"@"+myhost+":path$ ")
    bash(c)
    bashfun()

def main():
    usernamepas()
    testuserpass()

if __name__ == "__main__":
	main()
