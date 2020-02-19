import os
import time
bash=os.system

def sleep():
	while True:
		bash('scp /home/ifb/info.txt noah@10.183.5.254:/home/noah/html/noah/data/arduino-noah.txt')
		time.sleep( 10 )


def main():
	sleep()
	
if __name__ == "__main__":
	main()
