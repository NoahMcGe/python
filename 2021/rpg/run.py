#Noah McGe 10/21/2021 - 10/23/2021
import random
import time

adjectivelist=["Spicy","Angry","Cruel","Depressed","Evil","Foolish","Hungry","Jittery","Proud","Wicked","Wild"]
nounlist=["Beast","Wyvern","Goblin","Troll","Ogre","Dragon","Spider","Mummy","Wolf"]


class Player:
	def player_status(self):
		print("\n-- STATUS --" )
		print("Name:",self.name)
		print("Level:",self.level)
		print("EXP:",self.exp,"/",self.expmax)
		print("HP:",self.hp,"/",self.hpmax)
		print("Attack:",self.attack)
		print("Defence:",self.defence)
		print("Luck:",self.luck)
		
class Quest:
	def quest_status(self):
		print(self.name,"Kill",self.killamountneeded,self.montype+"s for a reward of:",self.reward,"exp")
		print("   You have killed:",self.killamount,"/",self.killamountneeded)

def guildmenu():
	print("\n---QUESTS---   Quests do not save with your player stats\n")
	try:
		quest1.quest_status()
		quest2.quest_status()
		quest3.quest_status()
	except:
		define_quest()
		quest1.quest_status()
		quest2.quest_status()
		quest3.quest_status()
	menu()

def define_quest():
	global quest1
	global quest2
	global quest3
	for i in range(1, 4):
		globals()['quest%s' % i] = Quest()
		globals()['quest%s' % i].name = "Quest "+str(i)
		globals()['quest%s' % i].montype = random.choice(nounlist)
		globals()['quest%s' % i].killamountneeded = random.randint(2,5)
		globals()['quest%s' % i].reward = globals()['quest%s' % i].killamountneeded*8+player1.level
		globals()['quest%s' % i].killamount = 0

def check_quest():
	try:
		quest1.name = quest1.name
	except:
		define_quest()


def define_player():
	global player1
	player1 = Player()
	player1.name = input("Player name: ")
	player1.level = 1
	player1.hpmax = 50
	player1.hp = player1.hpmax
	player1.expmax = 10
	player1.exp = 0
	player1.attack = 2.5
	player1.defence = 2
	player1.luck = random.randint(1,100)
	player1.skillpoints = 2
	player1.killcount = 0
	
	player1.player_status()
	
def define_monster():
	global monster1
	monster1 = Player()
	monster1.tagadj = random.choice(adjectivelist)
	monster1.tagnoun = random.choice(nounlist)
	monster1.name = monster1.tagadj+" "+monster1.tagnoun
	monster1.level = player1.level+random.randint(-3,5)
	if (monster1.level < 1):
		monster1.level=1
	monster1.hpmax = monster1.level*2 + 38+random.randint(-4,8)
	monster1.hp = monster1.hpmax
	monster1.expmax = 9+monster1.level
	monster1.exp = 0+random.randint(0,monster1.expmax-1)
	monster1.attack = monster1.level+monster1.level/2+random.randint(-5,5)
	monster1.defence = monster1.level+monster1.level/2 +random.randint(-5,5)
	if (monster1.defence < 1):
		monster1.defence = 1
	if (monster1.attack < 1):
		monster1.attack = 1
	monster1.luck = random.randint(1,100)
	


def gointodun():
	print("\nSearching for monsters...\n")
	time.sleep(random.randint(1,5))
	monsterchance = random.randint(1,100)
	monsterchance = monsterchance+player1.luck/1.5
	if (monsterchance > 60):
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
		p1tempdamage= player1.attack-monster1.defence/1.65
		m1tempdamage= monster1.attack-player1.defence
		critchance = random.randint(1,4000)+player1.luck*3
		if (critchance > 3900):
			p1tempdamage = player1.attack*1.5
			print("\nYou got a Critical hit! One of your attack ignored "+monster1.name+"'s armor.")
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
			critchance = random.randint(1,4000)+player1.luck*3
			p1tempdamage= player1.attack-monster1.defence/1.65
			m1tempdamage= monster1.attack-player1.defence
			if (critchance > 3900):
				p1tempdamage = player1.attack*1.5
				print("\nYou got a Critical hit! One of your attack ignored "+monster1.name+"'s armor.")
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
		menu()

def monsterkill():
	luckydrop = random.randint(0,1000)+player1.luck*3
	print(player1.name," did slay the beast!")
	if (luckydrop > 999):
		player1.skillpoints = player1.skillpoints+1
		print("\n--- YAHOOOOOO\nYOU GOT A LUCKY DROP, +1 SKILLPOINT\n--- YAHOOOOOOO\n")
	if (monster1.level > player1.level):
		player1.exp=2*monster1.level-player1.level+player1.exp+6
	else:
		player1.exp=player1.exp+4+monster1.level
	if (player1.exp > player1.expmax or player1.exp == player1.expmax):
		levelup()
	player1.killcount = player1.killcount+1
	for i in range(1, 4):
		if (monster1.tagnoun == globals()['quest%s' % i].montype):
			globals()['quest%s' % i].killamount = globals()['quest%s' % i].killamount +1
			if (globals()['quest%s' % i].killamount == globals()['quest%s' % i].killamountneeded):
				print(globals()['quest%s' % i].name,"has been completed!!!")
				globals()['quest%s' % i].quest_status()
				player1.exp = player1.exp + globals()['quest%s' % i].reward
				globals()['quest%s' % i].montype = random.choice(nounlist)
				globals()['quest%s' % i].killamountneeded = random.randint(2,5)
				globals()['quest%s' % i].reward = globals()['quest%s' % i].killamountneeded*8+5
				globals()['quest%s' % i].killamount = 0
				if (player1.exp > player1.expmax or player1.exp == player1.expmax):
					levelup()
				
	menu()
		
def levelup():
	if (player1.exp > player1.expmax or player1.exp == player1.expmax):
		player1.level=player1.level+1
		player1.exp = player1.exp-player1.expmax
		player1.expmax = 10+2*player1.level
		player1.attack = player1.attack+1.5
		player1.defence = player1.defence+1
		player1.hpmax = player1.hpmax+2
		player1.hp = player1.hpmax
		player1.skillpoints = player1.skillpoints+1
		print("\nLEVEL UP\n")
		levelup()
		
def skillpointmenu():
	print("\n---SKILL POINT MENU---\n",player1.name,"has:",player1.skillpoints,"Skillpoints!")
	print(" Monster Kill Count:",player1.killcount)
	print("\n1. Add HP (+2)\n2. Add Attack (+1)\n3. Add Defence (+1)\n4. Add Luck (+3)\n5. Full HP\n6. Back")
	if (player1.skillpoints==0):
		print("you must leave this menu if you have no skillpoints")
		menu()
	pick = input("Choose: ")
	if (pick=="1"):
		player1.hpmax=player1.hpmax+2
		player1.hp=player1.hp+2
		player1.skillpoints = player1.skillpoints-1
		print("2 hp has been added to your stats!")
		menu()
	elif (pick=="2"):
		player1.attack=player1.attack+1
		player1.skillpoints = player1.skillpoints-1
		print("1 attack has been added to your stats!")
		menu()
	elif (pick=="3"):
		player1.defence=player1.defence+1
		player1.skillpoints = player1.skillpoints-1
		print("1 defence has been added to your stats!")
		menu()
	elif (pick=="4"):
		player1.luck=player1.luck+3
		player1.skillpoints = player1.skillpoints-1
		print("3 luck has been added to your stats!")
		menu()
	elif (pick=="5"):
		player1.hp=player1.hpmax
		player1.skillpoints = player1.skillpoints-1
		print("You have been refreshed!")
		menu()
	elif (pick=="6"):
		menu()
	else:
		print("that option is not available")
		skillpointmenu()

def monsterfound():
	print("\n-- OPTIONS --\n1. Flee\n2. Fight\n3. Fight to the death! \n4. View Monster Status\n5. View ",player1.name,"'s Status")
	pick = input("Choose: ")
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

def savefile():
	f = open('savefile.txt','w')
	f.write(player1.name+"\n"+str(player1.level)+"\n"+str(player1.exp)+"\n"+str(player1.expmax)+"\n"+str(player1.hp)+"\n"+str(player1.hpmax)+"\n"+str(player1.attack)+"\n"+str(player1.defence)+"\n"+str(player1.luck)+"\n"+str(player1.skillpoints)+"\n"+str(player1.killcount))
	f.close()
	print("\nsaved to current directory: savefile.txt")

def openfile():
	f = open('savefile.txt','r')
	fileline = f.readlines()
	player1.name = str(fileline[0]).strip()
	player1.level = int(fileline[1])
	player1.exp = int(fileline[2])
	player1.expmax = int(fileline[3])
	player1.hp = float(fileline[4])
	player1.hpmax = int(fileline[5])
	player1.attack = float(fileline[6])
	player1.defence = float(fileline[7])
	player1.luck = int(fileline[8])
	player1.skillpoints = int(fileline[9])
	player1.killcount = int(fileline[10])
	f.close()
	print("\nopened from current directory: savefile.txt")
	check_quest()


def menu():
	print("\n-- OPTIONS --\n1. See Satus\n2. Go into the dungeon\n3. Skill Menu\n4. Quests\n5. Save\n6. Open Save\n7. Reset")
	pick = input("Choose: ")
	if (pick == "1"):
		player1.player_status()
		menu()
	elif (pick == "2"):
		check_quest()
		gointodun()
	elif(pick=="3"):
		skillpointmenu()
	elif(pick=="4"):
		guildmenu()
	elif(pick=="5"):
		try:
			savefile()
		except:
			print("\nsave failed!!")
		menu()
	elif(pick=="6"):
		try:
			openfile()
		except:
			print("\nopening save failed!!")
		menu()
	elif(pick=="7"):
		main()
	else:
		print("Option not available")
		menu()

def main():
	print("Starting ...\n")
	define_player()
	menu()
	print("\nGAME OVER")
	
main()
		
