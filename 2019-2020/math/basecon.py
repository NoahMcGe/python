#basecon.py :)

def bincon(num, addspace):
	n = num
	s = addspace
	#print(n, s)
	#print(n, end = " = ")
	d = 128
	binString = ""
	for i in range (0,8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString + str(q)
		if(s == 1 and i == 3):
			binString = binString + " "
	#print(binString)
	return binString

def main(addaspacemaybe):
	bs = ""
	bs = bincon(151, int(addaspacemaybe))
	print(str(152) + " =", str(bs))

aspaceting = input("Do you want a nice l1l space (y/n)? ")
space = 0
if (aspaceting == "y"):
	space = 1
else:
	space = 0
main(space)
