#noahmcge
'''
Enter Temperature: 50
Enter Temperature: 50.1
Sum = 100.1
'''
def forn1():
	global sum1
	global a
	sum1 = 0 #setting a var
	a = 0 #setting a var
	while1() #telling python to the the "while1" function
	
def while1():
	global sum1
	global a
	while(a < 10):
		try:
			b=input("Enter Temperature: ")
			sum1 = sum1 + float(b)
			a = a+1
		except:
			print("Please enter numbers only")
			while1()
	if (a == 10):
		print("Sum = ",sum1)
		quit()
			

def main():#The main function tells python to the the "forn1" function
	forn1()

if __name__ == "__main__": #this is the 1st thing the code runs, it tells python to the the "main" function
    main()
 
