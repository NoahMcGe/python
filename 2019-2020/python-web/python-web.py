import http.server
import socketserver
import os

def webstart():
	bigline="----------------------------------"
	PORT = input("What Port would you like to use?: ")
	PORT = int(PORT)
	webroot = input("What folder to use as web root?: ")
	web_dir = os.path.join(os.path.dirname(__file__), webroot)
	os.chdir(web_dir)#web root
	Handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), Handler)
	print(bigline)
	print("serving at port", PORT)
	print("Webroot is "+webroot+'/')
	print(bigline)
	httpd.serve_forever()
	

def main():
	webstart()

if __name__ == "__main__":
    main()
