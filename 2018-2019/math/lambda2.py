#file 2 : lambda2.py noah mcgehee
def myfunc(n):
	return lambda a : a * n

my2x = myfunc(2)
my3x = myfunc(3)
dub = my2x(2)

print(my2x(11))
print(my3x(11))
print("dub", dub)
