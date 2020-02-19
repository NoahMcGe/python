##############
## Script listens to serial port and writes contents into a file
##############
## requires pySerial to be installed 
#sudo apt install python-serial
#python2 not python3
import serial
import sys
import os

bash=os.system
serial_port = '/dev/ttyACM0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
ser = serial.Serial(serial_port, baud_rate)
def info():
	global line
	while True:
		line = ser.readline();
		line = line.decode("utf-8") #ser.readline returns a binary, convert to string
		print(line)
		bash('echo "' + line + '" >> /home/ifb/info.txt')
		#bash('scp info.txt noah@10.183.5.254:/home/noah/html/noah/data/arduino-noah.txt')



def main():
	info()
	
if __name__ == "__main__":
	main()
