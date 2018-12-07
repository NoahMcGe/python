'''
multiplication table printer
'''
#multiplication.py noah m
def multi_table(a):
	
	for i in range(1,21):
		print('{0} x {1} = {2}'.format(a,i,a*i))

if __name__== '__main__':
	a = input('welcome to good burger home of the good burger may i take your order?!?: ')
	multi_table(float(a))

