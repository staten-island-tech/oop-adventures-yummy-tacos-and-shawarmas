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

    def health(self):
        if self.hunger <=0 or self.sleep <= 0 or self.thirst <= 0:
            self.health -= 10
            self.strength -= 10
            self.stamina -= 10
        for healing in self.inventory:
            self.health += 50