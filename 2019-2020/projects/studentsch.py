'''
thank youuuuu ezekiel
'''

fn = input("What is your Nimble Name? ")
ln = input("What is your Goof name? ")
id = int(input("How Old is you: "))
longL = "/ \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ / \ "
openL = "|                                             |"
print(longL)
print(openL)
print("|\t" + ln + ", " + fn + "\t\tAge: " +str(id) + "      |")
print(openL)
print(longL)
print(openL)
sub = " "
room = 0
c = 1
while (sub != "STOP"):
    sub = input("Enter the next class, STOP to end: ")
    if (sub != "STOP"):
        room = int(input("Enter the room number: "))
        print("*\tBlock " + str(c) + ": " + sub + "\tRoom: " + str(room) + " \t*")
        c = c + 1
print(openL)
print(longL)
print(openL)
print(longL)
