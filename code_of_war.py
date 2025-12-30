import random
class game:
	def __init__(self,name):
		self.name = name
		self.life = 20

	def attack(self,enemy,ran_no):
		enemy.life = enemy.life - ran_no

	def checklife(self,enemy):
		print(f"{enemy.name} LIFE = {enemy.life} LEFT")
		print(f"YOUR LIFE = {self.life} LEFT")

print("-----WELCOME TO CODE OF WAR GAME💥💥-----")
print("                                          ")
pla1 = input("ENTER THE NAME OF PLAYER 1 : ")
pla2 = input("ENETR THE NAME OF PLAYER 2 : ")
print("                                          ")
print("---------------GAME START🏁---------------")

ob1 = game(pla1)
ob2 = game(pla2)

chance = True
while ob1.life >= 0 and ob2.life >= 0:
	a = random.randint(1,10)
	if chance == True:
		WE = input(f"{ob1.name} ENTER 1 FOR ATTACK 🚀 :-  ")
		print("ATTACK ❗❗ SUCCESSFUL💢")
		print(f"DAMAGE TO {ob2.name} = {a}")
		ob1.attack(ob2,a)
		ob1.checklife(ob2)
		print("                                          ")
		chance = False
	else:
		WE = input(f"{ob2.name} ENTER 2 FOR ATTACK 🚀 :-  ")
		print("ATTACK ❗❗ SUCCESSFUL💢")
		print(f"DAMAGE TO {ob1.name} = {a}")
		ob2.attack(ob1,a)
		ob2.checklife(ob1)
		print("                                          ")
		chance = True

if ob1.life < ob2.life:
	print("🤩🤩")
	print(f"{ob2.name} WON THE GAME {ob2.life} LIFE LEFT")
else:
	print("🤩🤩")
	print(f"{ob1.name} WON THE GAME, {ob1.life} LIFE LEFT")

exit = input("----------HIT ENTER FOR EXIT :")







