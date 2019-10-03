#bincon_loop.py  :)
n = int(input("Input an interger < 256: "))
d = 128
n_original = n
binString = ""
for i in range (0,8):
  q = int(n / d)
  r = int(n % d)
  print ("dividend", end = " = ")
  print (d, end = ", ")
  print ("quotent", end = " = ")
  print (q, end = ", ")
  print ("remainder", end = " = ")
  print (r)
  
  n = r
  d = int(d / 2)
  binString = binString+str(q)
print("\n==============================\n")
print
print(str(n_original) + " in base 10 = " + binString + " base 2")
print("\n==============================")
