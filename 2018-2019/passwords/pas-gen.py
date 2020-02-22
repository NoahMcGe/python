import string
import random

def randompassword():
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
	size = random.randint(10, 20)
	return ''.join(random.choice(chars) for x in range(size))
p = randompassword
print (p)
