def numbershaha():
	for n in range(1,101):#N goes 1-100
		nu3=n%3#Seting Variable
		nu5=n%5#Setting Variable
		if (nu3 > 0 and nu5 > 0):#1 Prints number when Remainder of 3 or 5.
			print(n)
		elif(nu3==0 and nu5==0):#2 If both 3 and 5 have no Remainder then prints (has to be infront of both 3 and 4)
			print("FizzBuzz")
		elif(nu3==0):#3 If 3 has no Remainder prints
			print("Fizz")
		elif(nu5==0):#4 if 5 has no Remainder prints
			print("Buzz")


def main():
	numbershaha()


if __name__ == "__main__":
	main()
