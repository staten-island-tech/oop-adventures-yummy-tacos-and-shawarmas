import random

class Hero:
    def __init__(self, name, money, health, sleep, hunger, thirst, stamina, strength, inventory, speed):
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



RandomHero = Hero("Player_Choice", 50, 100, 100, 100, 100, 100, 5, [], 10)


def health(self):
        
        
    if RandomHero.hunger <= 0:
        RandomHero.health -= random.randint(5, 10)
        RandomHero.strength -= random.randint(5, 10)
        RandomHero.stamina -= random.randint(5, 10)
        print("You're getting very hungry. Eat some food, or else you will lose health, strength, and stamina.")
    elif RandomHero.thirst <= 0:
        RandomHero.health -= random.randint(5, 10)
        RandomHero.strength -= random.randint(5, 10)
        RandomHero.stamina -= random.randint(5, 10)
        print("You can't handle the dehydration anymore. Drink something, or you will start to lose health, strength, and stamina.")
    elif RandomHero.sleep <= 0:
        RandomHero.health -= random.randint(5, 10)
        RandomHero.strength -= random.randint(5, 10)
        RandomHero.stamina -= random.randint(5, 10)
        print("If you keep pulling all-nighters and not sleeping, you will die. Rest your eyes, or you will lose health, strength, and stamina.")




print(RandomHero.__dict__)

