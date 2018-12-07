# hexbincon.py noah m



ans=True
while ans:
    print ("""
    1.Dec to Binary
    2.Dec to hex
    3.Exit/Quit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
	  bincon(decimal)
    elif ans=="2":
	  cal(a)
    elif ans=="3":
      print("\n Goodbye") 
    elif ans !="":
      print("\n Not Valid Choice Try again") 




a=input("enter number in decimal :")
def cal(a):
    if a<10:
        b=str(a)
    elif a==10:
        b="A"
    elif a==11:
        b="B"
    elif a==12:
        b="C"
    elif a==13:
        b="D"
    elif a==14:
        b="E"
    else:
        b="F"
    return b
b=a
L1=""
while True:
    c=b%16
    if b<16:
        L1=L1+cal(c)
        break
    else:
        L1=L1+cal(c)
    b=b/16
c=""
for i in reversed(L1):
    c=c+i
print c




def bincon(decimal):
	print("BINARY\n")
	print (decimal)
	binstr=""
	for i in range(8):
		bin = decimal % 2
		binstr = binstr + str(bin)
		decimal = decimal // 2 
		print (bin)
	print(binstr)
	
def oof():
	print("INPUT -1 TO EXIT LOOP")
	print("INPUT AN INTEGER LESS THAN 256 AND GREATER THAN -1")
	done = 0;
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
oof()





