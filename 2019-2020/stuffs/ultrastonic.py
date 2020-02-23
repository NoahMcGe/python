# Noah McGehee 
# https://github.com/NoahMcGe
# 2/22/2020


#requires pySerial to be installed 
#sudo apt install python-serial
#python2 not python3
#python3 doesnt not let you import serial kinda huge lame ## DO THIS FOR PYTHON3 $ sudo apt install python3-pip  $ sudo pip3 install pyserial
import serial


# READ ME
# to use with ultra sonic thingy, only works in linux
# Uncomment
# Comment line 135
# Uncomment line 136
# Uncomment line 133
# Uncomment line 132
# Uncomment line 38
# Uncomment line 39
# Uncomment line 40


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
#serial_port = '/dev/ttyACM0';
#baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
#ser = serial.Serial(serial_port, baud_rate)
line=""

def year():
	global dt
	dt = datetime.datetime.now()
	y = dt.year
	timestring = str(y)
	return timestring
def month():
	global dt
	dt = datetime.datetime.now()
	m = dt.month
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def day():
	global dt
	dt = datetime.datetime.now()
	m = dt.day
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def hour():
	global dt
	dt = datetime.datetime.now()
	m = dt.hour
	if (int(m)<10):
		m=str("0")+str(m)
	timestring = str(m)
	return timestring
def stmin():
	global dt
	dt = datetime.datetime.now()
	m = dt.minute
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
'''
def getDateStringfile():
	global dt
	dt = datetime.datetime.now()
	y = dt.year
	hr = dt.hour
	if hr < 10:
		hr = "0" + str(hr)
	me = dt.minute
	if me < 10:
		me = "0" + str(me)
	timestring = str(dt.day)+"-"+str(hr)+'-'+str(me)
	return timestring

def getDateStringfolder():
	dt = datetime.datetime.now()
	y = dt.year
	timestring = str(dt.month) +'-'+ str(dt.day)+'-' + str(y)
	return timestring
	'''
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




def sleepeyedjohn():
	time.sleep(30)
	Cred="Made By NoahMcGehee \nhttps://github.com/NoahMcGe"
	return Cred

def info():
	global line
	time.sleep(3)
	while True:
		#line = ser.readline();
		#line = line.decode("utf-8") #ser.readline returns a binary, convert to string
		print(line)
		bash('echo "Second: '+secdt()+' - Distance: '+sleepeyedjohn()+'" >> /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/'+'Ultra-Sonic.txt')
		#bash('echo "Second: '+secdt()+' - Distance: '+line + '" >> /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/'+'Ultra-Sonic.txt') # uncomment this line for use in ultra sonic thingy
		#just testing rn so it is commented out dont want my storage to fill up that quick

def folderpidata():
	bash('cd /home/'+username+';mkdir pi-data')



def foldermin():
	bash('mkdir /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+' -p')
	bash('cd /home/'+username+'/pi-data/;echo "Folder Layout, YEAR>MONTH>DAY>24HOUR>MIN>Document" > folder-layout.txt')
	while True:
		if (int(secdt()) == 0):
			bash('mkdir /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+' -p')
		elif(int(secdt()) == 60):
			print("Here it comes!")
		else:
			print(getDateStringfolder2())
			print('Seconds: '+ secdt())
			print("Made By Noah McGehee")
			time.sleep(0.85)#this is so it doesnt eat the cpu alive for no good reason, Your welcome lul

def pushtoserver():#Make sure you can ssh login without a password or this will be a huge pain
	time.sleep(5)
	bash('scp -r /home/'+username+'/pi-data/'+'/ draven@192.168.1.10:/home/draven/scp/pi/data/')
	#bash('scp -r /home/'+username+'/pi-data/'+'/ noah@10.183.5.254:/home/noah/html/pi/data/')
	while True:
		bash('scp -r /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/ draven@192.168.1.10:/home/draven/scp/pi/data/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/')
		#bash('scp -r /home/'+username+'/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/'+stmin()+'/ noah@10.183.5.254:/home/noah/html/pi/data/pi-data/'+year()+'/'+month()+'/'+day()+'/'+hour()+'/')
		time.sleep( 3 )



	'''
def foldermin():
	bash('cd /home/'+username+'/pi-data/;mkdir '+getDateStringfolder()+';cd '+getDateStringfolder()+';mkdir '+getDateStringfolder2())
	while True:
		if (int(secdt()) == 0):
			bash('mkdir /home/'+username+'/pi-data/'+getDateStringfolder()+'/'+getDateStringfolder2()+' -p')
		elif(int(secdt()) == 60):
			print("Here it comes!")
		else:
			print('Seconds: '+ secdt())
			print(getDateStringfolder2())
			print("Made By Noah McGehee")
			time.sleep(0.85)#this is so it doesnt eat the cpu alive for no good reason, Your welcome lul

def pushtoserver():
	while True:
		bash('scp -r /home/'+username+'/pi-data/'+getDateStringfolder()+'/ noah@10.183.5.254:/home/noah/html/pi/data/')
		time.sleep( 30 )
'''

def main():
	folderpidata()
	thread1 = Thread(target=foldermin)
	thread2 = Thread(target=info)
	thread3 = Thread(target=pushtoserver)
	thread1.start()
	thread2.start()
	thread3.start()
	
if __name__ == "__main__":
	main()
