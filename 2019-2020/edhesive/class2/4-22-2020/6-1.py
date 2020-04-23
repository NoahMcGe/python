#noahmcge
#1: You entered _____

def forn1():
	a=1
	i=1
	b = input("Please enter the next word: ")
	while 1:
		if(a == 1):
			print("#"+str(i) + ": You entered "+b)
			b = input("Please enter the next word: ")
			if (b == "stop" or b =="Stop" or b =="STOP"):
				a = 2
				print("All done. "+str(i)+" words entered.")
			i = i+1
		if (b == "stop" or b =="Stop" or b =="STOP"):
			quit()
			
		

def main():
	forn1()

if __name__ == "__main__":
    main()
 
