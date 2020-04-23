def numbershaha():
	numa = input("Number 1 : ")
	numb = input("Number 2 : ")
	for n in range(1,101):#N goes 1-100
		nu1=n%int(numa)#Seting Variable
		nu2=n%int(numb)#Setting Variable
		if (nu1 > 0 and nu2 > 0):#1 Prints number when Remainder of numa or numb.
			print(n)
		elif(nu1==0 and nu2==0):#2 If both numa and numb have no Remainder then prints (has to be infront of both 3 and 4)
			print(str(n)+" : has a Factor of both "+numa+" "+numb)
		elif(nu1==0):#3 If numa has no Remainder prints
			print(str(n)+" : has a Factor of "+numa)
		elif(nu2==0):#4 if numab has no Remainder prints
			print(str(n)+" : has a Factor of "+numb)


def main():
	numbershaha()


if __name__ == "__main__":
	main()
