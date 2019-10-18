
def roots(a,b,c):
    D = (b*b - 4*a*c)
    print()
    print("D = " + str(D))
    if (D >= 0): #check for positive D
            print ("REAL ROOTS")
            D = D**0.5 # calculate square root of D
            x1 = (-b + D) / (2*a)
            x2 = (-b - D) / (2*a)
            print ("x1 = "+str(x1)+" x2 = "+str(x2))

    elif(D < 0): #check for negative D
            D = (D * -1)**0.5; #Change D to a positive.
            # Take square root of D then represent with "i"
            print("IMAGINARY ROOTS")
            print ("1x = -"+str(b/(2*a))+" - "+str(D/(2*a))+"i")
            print ("1x = -"+str(b/(2*a))+" + "+str(D/(2*a))+"i")
#The following has two underscores__ before and after name and main
if __name__ == '__main__':
        print("Input a,b and c for the quadratic (ax^2 + bx + c)")
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")
        roots(float(a), float(b), float(c))
'''
Input a,b and c for the quadratic (ax^2 + bx + c)
Enter a: 5
Enter b: 4
Enter c: 2

D = -24.0
IMAGINARY ROOTS
1x = -0.4 - 0.4898979485566356i
1x = -0.4 + 0.4898979485566356i

'''
