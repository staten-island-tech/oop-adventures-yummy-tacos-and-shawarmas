import random

class Hero:
    def __init__(self, name, money, health, sleep, hunger, thirst, stamina, strength, inventory, speed, damage):
        self.name = name
        self.money = money
        self.health = health
        self.sleep = sleep
        self.hunger = hunger
        self.thirst = thirst
        self.stamina = stamina
        self.strength = strength
        self.inventory = inventory
        self.speed = speed
        self.damage = damage

RandomHero = Hero("Player_Choice", 50, 100, 100, 100, 100, 100, 5, [], 10, 10)
RandomHero.name = input("What would you like to name your brave adventurer? Don't worry about your choice, it can be changed later.")

while True:

    if RandomHero.hunger <= 0:
        RandomHero.health -= random.randint(5, 10)
        print("You're getting very hungry. Your stomach growls and starts eating itself. Eat something quick before you start to wither away.")
        break

    elif RandomHero.thirst <= 0:
        RandomHero.health -= random.randint(5, 10)
        print("You are dehydrated. Drink something or else you will start to take damage.")
        break

    elif RandomHero.sleep <= 0:
        RandomHero.health -= random.randint(5, 10)
        print("You need sleep because you keep pulling all-nighters. Rest now or you will lose health.")
        break

    elif RandomHero.health <= 0:
        print("Your health has fully depleated. You can no longer move and fall to the ground and die. GAME OVER!")
        quit()
    
    elif RandomHero.money <= 0:
        print("You should go fight monsters to get some money. Or you could sell some items in the store for money.")
        break

    elif RandomHero.stamina <= 0:
        RandomHero.speed -= 3
        print("You feel very tired after walking for too long. You start to become slower while trying to walk. Go to the gym to get more stamina.")
        break

    elif RandomHero.strength <= 0:
        RandomHero.damage -= 2
        print("Your muscles feel very weak and are aching. Your low strenth starts to decrease your damage. Fight monsters or go to the gym to get more strength.")
        break

print(RandomHero.__dict__)

