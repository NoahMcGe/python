##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
#sudo apt install python-serial
#python2 not python3
import serial
import sys
import os
import datetime
import socket
import getpass


username = getpass.getuser()
myhost = os.uname()[1]
bash=os.system
serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
ser = serial.Serial(serial_port, baud_rate)


def getDateStringfile():
	dt = datetime.datetime.now()
	y = dt.year - 2000 
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
	y = dt.year - 2000 
	hr = dt.hour
	if hr < 10:
		hr = "0" + str(hr)
	me = dt.minute
	if me < 10:
		me = "0" + str(me)
	timestring = str(dt.month) +'-'+ str(dt.day)+'-' + str(y)
	#timestring = str(y) + str(dt.month) + str(dt.day)
	return timestring



def info():
	global line
	while True:
		filename = getDateStringfile()
		foldername = getDateStringfolder()
		line = ser.readline();
		line = line.decode("utf-8") #ser.readline returns a binary, convert to string
		print(line)
		bash('cd /home/'+username+';mkdir pi-data')
		bash('cd /home/'+username+'/pi-data/;mkdir '+foldername)
		bash('echo "' + line + '" >> /home/'+username+'/pi-data/'+foldername+'/'+filename+'.txt')
		#bash('scp info.txt noah@10.183.5.254:/home/noah/html/noah/data/arduino-noah.txt')

def info2():
	bash('cd /home/'+username+';mkdir pi-data')

def main():
	info2()
	info()
	
if __name__ == "__main__":
	main()
