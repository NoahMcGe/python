#file 3 : quadratic_lambda.py noahmcgehee

def quadtratic_funcation(a,b,c):
	return lambda x: a*(x**2) + b*x + c
	
a1 = quadtratic_funcation(1,2,1)
#print(a1(1))
print("Input a,b and c from a quadratic equation in the form of ")
print("f(x) = ax^2 + bx + c")
#we have a problem here
a = float(input ("Input a "))
b = float(input ("Input b "))
c = float(input ("Input c "))
x = float(input ("Input x "))
a2 = quadtratic_funcation(a,b,c)
fx = a2(x)
print("f(x) = ",fx)
