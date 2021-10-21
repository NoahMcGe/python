#Noah McGe 10/21/2021
import random
import time

class Player:
	def player_status(self):
		print("\n-- STATUS --" )
		print("Name: "+self.name)
		print("Level:",self.level)
		print("EXP:",self.exp,"/",self.expmax)
		print("HP:",self.hp,"/",self.hpmax)
		print("Attack:",self.attack)
		print("Defence:",self.defence)
		print("Luck:",self.luck)
				
def define_player():
	global player1
	player1 = Player()
	player1.name = input("Player name: ")
	player1.level = 1
	player1.hpmax = player1.level*2 + 48
	player1.hp = player1.hpmax
	player1.expmax = 10
	player1.exp = 0
	player1.attack = 1+player1.level+player1.level/2
	player1.defence = player1.level+player1.level/2 -0.5
	player1.luck = random.randint(1,100)
	player1.skillpoints = 0
	
	player1.player_status()
	
def define_monster():
	global monster1
	monster1 = Player()
	#monster1.name = random.randrange("Mad Cow","Young Beaver","Samskwanch") broken/ fix later
	monster1.name = "Mad Cow"
	monster1.level = player1.level+random.randint(0,7)-2
	if (monster1.level < 1):
		monster1.level=1
	monster1.hpmax = monster1.level*2 + 38
	monster1.hp = monster1.hpmax
	monster1.expmax = 9+monster1.level
	monster1.exp = 0+random.randint(0,monster1.expmax-1)
	monster1.attack = monster1.level+monster1.level/2-1
	monster1.defence = monster1.level+monster1.level/2 -2
	if (monster1.defence < 1):
		monster1.defence = 1
	if (monster1.attack < 1):
		monster1.attack = 1
	monster1.luck = random.randint(1,100)
	


def gointodun():
	print("\nSearching for monsters...\n")
	time.sleep(random.randint(1,7))
	monsterchance = random.randint(1,100)
	monsterchance = monsterchance+player1.luck/1.5
	if (monsterchance > 75):
		print("MONSTER FOUND! PREPARE YOURSELF D:<")
		define_monster()
		monster1.player_status()
		monsterfound()
	else:
		print("Bad luck! No Monsters Found....")
		menu()
		
def playervsmonster():
	if (player1.hp > 1):
		if (player1.attack < monster1.defence/1.5):
			print("\n you are too weak to deal damage to ",monster1.name)
			escape()
		if (monster1.attack < player1.defence):
			print("\n The sight of you put ",monster1.name,"in to shock and it has died from fear")
			monsterkill()
		print("OUCH you hit each other!\n")
		p1tempdamage= player1.attack-monster1.defence/1.5
		m1tempdamage= monster1.attack-player1.defence
		player1.hp = player1.hp - m1tempdamage
		monster1.hp = monster1.hp - p1tempdamage
		print(player1.name," did ",p1tempdamage," to ",monster1.name)
		print(monster1.name," did ",m1tempdamage," to ",player1.name)
		if (monster1.hp < 1):
			monsterkill()
		monsterfound()
	else:
		print("\nYou can not fight.. you are a ghost!")
		menu()
	
def playervsmonster2death():
	if (player1.hp > 1):
		if (monster1.hp > 1):
			if (player1.attack < monster1.defence/1.5):
				print("\n you are too weak to deal damage to ",monster1.name)
				escape()
			if (monster1.attack < player1.defence):
				print("\n The sight of you put ",monster1.name,"in to shock and it has died from fear")
				monsterkill()
			p1tempdamage= player1.attack-monster1.defence/1.5
			m1tempdamage= monster1.attack-player1.defence
			player1.hp = player1.hp - m1tempdamage
			monster1.hp = monster1.hp - p1tempdamage
			playervsmonster2death()
		else:
			monsterkill()
	else:
		death()
		print("\nYou died... while fighting ",monster1.name)
	monsterfound()

def checkplayervsmonster2death():
	if (player1.hp < 1):
		print("\nYou can not fight.. you are a ghost!")
		menu()
	else:
		print("\nIt was a long fought battle... ")
		playervsmonster2death()

def death():
	time.sleep(1)
	player1.name = player1.name + " (Dead)"
	player1.hp = 0
	
def escape():
	if (player1.hp > 1):
		print("\nAttempting Escape!!")
		escapechance = random.randint(1,100)
		escapechance = escapechance + player1.luck/2.5
		if (escapechance > 50):
			time.sleep(1)
			print("\nEscaped ALIVE!\n")
			menu()
		else:
			death()
			print("\nYou died trying to escape...")
			menu()
	else:
		print(player1.name,"the ghost, flew away..")

def monsterkill():
	print(player1.name," did slay the beast!")
	if (monster1.level > player1.level):
		player1.exp=player1.exp+monster1.level-player1.level+5
	else:
		player1.exp=player1.exp+4+monster1.level
	if (player1.exp > player1.expmax or player1.exp == player1.expmax):
		levelup()
	menu()
		
def levelup():
	if (player1.exp > player1.expmax or player1.exp == player1.expmax):
		player1.level=player1.level+1
		player1.exp = player1.exp-player1.expmax
		player1.expmax = 10+2*player1.level
		player1.attack = 1+player1.level+player1.level/2
		player1.defence = player1.level+player1.level/2 -0.5
		player1.hpmax = player1.level*2 + 48
		player1.hp = player1.hpmax
		player1.skillpoints = player1.skillpoints+1
	print("\nLEVEL UP\n")
		

def monsterfound():
	print("\n-- OPTIONS --\n1. Flee\n2. Fight\n3. Fight to the death! \n4. View Monster Status\n5. View ",player1.name,"'s Status")
	pick = input("Chose: ")
	if (pick == "1"):
		escape()
	elif (pick =="2"):
		playervsmonster()
	elif (pick =="3"):
		checkplayervsmonster2death()
	elif (pick =="4"):
		monster1.player_status()
		monsterfound()
	elif (pick =="5"):
		player1.player_status()
		monsterfound()
	else:
		print("Option not available")
		monsterfound()

def menu():
	print("\n-- OPTIONS --\n1. See Satus\n2. Go into the dungeon")
	pick = input("Chose: ")
	if (pick == "1"):
		player1.player_status()
		menu()
	elif (pick == "2"):
		gointodun()
	else:
		print("Option not available")
		menu()
	
def main():
	print("Starting ...\n")
	define_player()
	menu()
	print("\nGAME OVER")
	
main()
		
