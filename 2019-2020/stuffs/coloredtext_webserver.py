# almost all code from preston, minus the webserver stuff from noah mcgehee + coleman
#  and some modifications to that code from noah mcgee. Thanks to them for help
#Noah - Changing for redhat, not debian.
#Noah - YOU MUST BE A MEMBER OF THE SUDO GROUP "WHEEL" TO RUN THIS CORRECTLY
#Noah - colorama MUST BE INSTALLED FOR REDHAT, pip3 install colorama
#Noah - termcolor MUST BE INSTALLED FOR REDHAT, pip3 install termcolor

import http.server
import socketserver
import os 
import sys
bashcmd = os.system

def error(problem, text2, color, blink):#this is mucho epico
    from colorama import Fore, Back, Style 
    from termcolor import colored, cprint 
    text1 = ''
    if (blink == True):
        text1 = colored('[' + problem + ']', color, attrs=['blink', 'bold']) 
    else:
        text1 = colored('[' + problem + ']', color, attrs=['bold']) 
    print(text1, end="") 
    #print(Fore.RED + '[' + problem + ']', end="") 
    print(Style.RESET_ALL, end=" ") 
    print(text2)

'''
def check_for_module(offical_name, module_name):
    installed = False
    try:
        import offical_name
    except ImportError as e:
        bashcmd('sudo apt install ' + module_name)#pass  # module doesn't exist, deal with it.
        bashcmd('clear')
        installed = True
    if (installed == True):
        error('SUCCESS', 'Installed ' + module_name, 'green', False)
'''

def bigline_seperator():
    from colorama import Fore, Back, Style 
    from termcolor import colored, cprint 
    color = 'blue'
    bigline="---------------------------------------"
    text1 = colored(bigline, color, attrs=['bold']) 
    print(text1)
    print(Style.RESET_ALL, end="") 

def main():
    try:
        try:
            PORT = input("What Port would you like to use?: ")
            PORT = int(PORT)
        except ValueError as e:
            error('ERROR', 'ValueError: Please enter a number, not text', 'red', True)
            main()
        path = '.'
        bigline_seperator()
        error('LIST', 'These are the folders: ', 'green', False)
        files = os.listdir(path)
        #this finds all folders, or anything that doesn't have a period
        for name in files:
            if '.' in name: 
                print ('', end="")
            else:
                print(name)
        bigline_seperator()
        webroot = input("What folder to use as web root?: ")
        try:
            web_dir = os.path.join(os.path.dirname(__file__), webroot)
            os.chdir(web_dir)#web root
            Handler = http.server.SimpleHTTPRequestHandler
            httpd = socketserver.TCPServer(("", PORT), Handler)
            print("serving at port", PORT)
            print("Webroot is "+webroot+'/')
            httpd.serve_forever()
            error('SUCCESS', 'setup was successful')
        except FileNotFoundError as e:
            error('ERROR', "FileNotFoundError: that folder does't exsist", 'red', True)
            exit()
    except OSError as e:
        error('ERROR', "OSError: Program will now exit", 'red', True)
        exit()

#error('Success', 'Installed python3-colorama', 'green', False)
#error('Success', 'Installed python3-termcolor', 'green', False)

def check_for_installs():
    installed_colorama = False
    installed_termcolor = False
    try:
        import colorama
    except ImportError as e:
        bashcmd('sudo pip3 install colorama')
        bashcmd('clear')
        installed_colorama = True

    try:
        import termcolor
    except ImportError as e:
        bashcmd('sudo pip3 install termcolor')
        bashcmd('clear')
        installed_termcolor = True

    if (installed_colorama == True):
        error('SUCCESS', 'Installed python3-colorama', 'green', False)
    if (installed_termcolor == True):
        error('SUCCESS', 'Installed python3-termcolor', 'green', False)

if (__name__ == "__main__"):
    check_for_installs()
    main()
