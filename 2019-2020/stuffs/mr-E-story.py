def story():
	global name
	global age
	name = input("Hello what is your name? : ")
	age = input("Nice to meet you "+name+"! How old are you? : ")
	part2()
	
def part2():
	print("Name : "+name+"\nAge : "+age)
	a = input ("Does your information look correct? (Y/N): ")
	if (a == "Y" or a == "y"):
		part3()
	elif (a == "N" or a == "n"):
		print("\nPlease enter the correct information\n")
		story()
	else:
		print("\nPlease enter (Y/N) nothing else will do.\n")
		part2()

def part3():
	if(name=="Davy"or name=="davy" and age =="Dead" or age =="dead"):
		print("Born on a mountain top in Tennessee...")
	elif(name == "Noah" or name =="noah"):
		print("\nSet my line by the river bed. \nCaught 10 fish and I killed em dead.\nI cut'em and gut'em\nAnd toss the heads in the water to keep them cats'n gators fed.\n")
		if(int(age) == 18):
			print("Cool, I am "+age+" too!")
		elif (int(age) > 18):
			print("Lol, old man. If i were "+age+"...Nevermind.")
		elif (int(age) < 18):
			print("Back in my day...")
		else:
			print("what a stange age you have... "+age)
	elif(name=="Mr.E"):
		print("Have a might fine day "+name+"!")
		print("LOOOOL, YOU FELL FOR IT CX (INCERT LAUGHING EMOJIIIII)\n~~~~ : "+age+" : ~~~~\nIt may have taken 10 years but now we finally know the truth!")
	else:
		print("\nI've never known another "+name+"! Very very cool")
		print("\nMr. E talks about you alot, you very well may possibly be his favorite student.")
		if (int(age) > 18):
			print("\nLol, old man. If i were "+age+"...Nevermind.")
		elif (int(age) < 18):
			print("\nBack in my day...")
		elif (int(age)==18):
			print("\nVery very cool, I am also "+age)

def main():
	story()
if __name__ == "__main__":
	main()
