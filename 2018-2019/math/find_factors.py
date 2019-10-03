#find_factors.py noah m
'''
i will be finding the factors or integers
'''
def factors(b):
	
	for i in range(1, b+1):
		if b % i == 0:
			print(i)

if __name__ == '__main__':
	
	b = input('your number BUD!:' )
	b = float(b)
	
	if b > 0 and b.is_integer():
		factors(int(b))
	else:
		print('Wrong number guyson!')
