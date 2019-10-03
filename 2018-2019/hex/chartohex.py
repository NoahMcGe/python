import binascii
noah = binascii.hexlify(b'Steve Pi')
mcgehee = binascii.hexlify(b'Noah McGehee')
he = "HEX ="
line = "————————————————————————————————————————————————————————————————————"
print (line)
print ("Steve Pi")
print (he,noah)
print (line)
print ("Noah McGehee")
print (he,mcgehee)
print (line)
a = input("Input your own text : ")
f = binascii.hexlify(a.encode('utf-8'))
print ("HEX =",  f)
print (line)
