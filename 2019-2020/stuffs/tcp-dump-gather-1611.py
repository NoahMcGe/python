import os
import getpass
bash=os.system
username = getpass.getuser()


def main():
	bash("date")
	bash("mkdir tcpdump-class")
	for i in range(2,28):
		bash("cd tcpdump-class;wget 10.183.1."+str(i)+"/1611.pcap")
		bash("mv tcpdump-class/1611.pcap tcpdump-class/10.183.1."+str(i)+".pcap")


if __name__ == "__main__":
	main()
