# Noah McGehee 
# https://github.com/NoahMcGe
# 2/23/2020


#requires pySerial to be installed 
#sudo apt install python-serial
## ------------------- DO THIS FOR PYTHON3 $ sudo apt install python3-pip  $ sudo pip3 install pyserial -------------------##
#only for linux
#Run on reboot | $ crontab -e        @reboot /path/to/file/ultrasonic.py
#if arduino gets unplugged plug it back in and reboot


import serial
from picamera import PiCamera
import sys
import os
import datetime
import socket
import getpass
from threading import Thread
import time


dt = datetime.datetime.now()
username = getpass.getuser()
myhost = os.uname()[1]
bash=os.system
serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
ser = serial.Serial(serial_port, baud_rate)
line=""


def year():
	dt = datetime.datetime.now()
	y = dt.year
	timestring = str(y)
	return timestring
def month():
	dt = datetime.datetime.now()
	m = dt.month
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def day():
	dt = datetime.datetime.now()
	m = dt.day
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def hour():
	dt = datetime.datetime.now()
	m = dt.hour
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def stmin():
	dt = datetime.datetime.now()
	m = dt.minute
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def stmin2():
	dt = datetime.datetime.now()
	m = dt.minute
	m = m+1
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def secdt():
	dt = datetime.datetime.now()
	y = dt.second
	if (int(y)<10):
		y=str("0")+str(y)
	timestring = str(y)
	return timestring
def getDateStringfolder2():
	dt = datetime.datetime.now()
	y = dt.year
	hr = dt.hour
	minu = dt.minute
	if hr < 10:
		hr = "0" + str(hr)
	me = dt.minute
	timestring = 'Day: '+str(dt.day)+" - Hour: "+str(hr)+' - Minute: '+str(minu)
	return timestring





'''
def camerafilename():
	#imagename="Image"+secdt()+".jpg"
	return "Image"+secdt()+".jpg"
	


def camerapi():
	#Camera Setup
	camera = PiCamera()
	camera.resolution = (1920, 1080)
	camera.rotation = 180
	#Picture 1
	#camera.start_preview()
	camera.capture('/home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/'+camerafilename())
	#camera.stop_preview()
'''


def sleepeyedjohn():
	time.sleep(1)
	Cred="Made By NoahMcGehee \nhttps://github.com/NoahMcGe"
	return Cred

def info():
	global line
	time.sleep(1)
	while True:
		line = ser.readline();
		line = line.decode("utf-8") #ser.readline returns a binary, convert to string
		bash('echo "Second: '+secdt()+' - Distance: '+line + '" >> /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/'+'Ultra-Sonic.txt')
		if (int(secdt())==0):
			bash('scp -r /home/'+username+'/pi-data/'+'/ noah@192.168.1.10:noah@10.183.5.254:/home/noah/html/pi/data/')
			bash('rm /home/'+username+'/pi-data/ -dR')
			bash('mkdir /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+' -p')
			bash('cd /home/'+username+'/pi-data/;echo "Folder Layout, YEAR>MONTH>DAY>24HOUR>MIN>Doc" > folder-layout.txt')
		#if (int(line) < 50):
			#camerapi()			
		#bash('echo "Second: '+secdt()+' - Distance: '+line + '" >> /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/'+'Ultra-Sonic.txt') # uncomment this line for use in ultra sonic thingy

def folderpidata():
	bash('cd /home/'+username+';mkdir pi-data')



def foldermin():
	bash('mkdir /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+' -p')
	bash('cd /home/'+username+'/pi-data/;echo "Folder Layout, YEAR>MONTH>DAY>24HOUR>MIN>Document" > folder-layout.txt')
	while True:
		if (int(secdt()) == 50):
			bash('mkdir /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin2()+' -p')
		elif(int(secdt()) == 58):
			bash('mkdir /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin2()+' -p')
			bash('scp -r /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/ noah@10.183.5.254:/home/noah/html/pi/data/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/')
		else:
			print(getDateStringfolder2())
			print('-----------------------------------------------')
			print('Seconds: '+ secdt())
			print('-----------------------------------------------')
			print("Made By Noah McGehee")
			time.sleep(0.85)#this is so it doesnt eat the cpu alive for no good reason, Your welcome lul
'''
def pushtoserver():#Make sure you can ssh login without a password or this will be a huge pain
	time.sleep(5)
	#bash('scp -r /home/'+username+'/pi-data/'+'/ draven@192.168.1.10:/home/draven/scp/pi/data/')
	bash('scp -r /home/'+username+'/pi-data/'+'/ noah@10.183.5.254:/home/noah/html/pi/data/')
	while True:
		#bash('scp -r /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/ draven@192.168.1.10:/home/draven/scp/pi/data/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/')
		bash('scp -r /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/ noah@10.183.5.254:/home/noah/html/pi/data/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/')
		time.sleep( 3 )
'''

def main():
	folderpidata()
	thread1 = Thread(target=foldermin)
	thread2 = Thread(target=info)
	#thread3 = Thread(target=pushtoserver)
	thread1.start()
	thread2.start()
	#thread3.start()
	
if __name__ == "__main__":
	main()
