import random

class Character:
    def __init__(self, name, health, stamina, strength, speed, damage):
        self.name = name
        self.health = health
        self.stamina = stamina
        self.strength = strength
        self.speed = speed
        self.damage = damage
    
    def is_alive(self):
        return self.health > 0
    

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 100, 100, 5, 10, 10)
        self.money = 50
        self.hunger = 100
        self.thirst = 100
        self.sleep = 100
        self.inventory = []
    
    def eat(self, item):
        self.hunger = min(100, self.hunger + item.effect)
        print(f"You eat {item.name}. Your hunger was restored.")

    def drink(self, item):
        self.thirst = min(100, self.thirst + item.effect)
        print(f"You drink {item.name}. Your thirst was restored.")

    def show_stats(self):
        print("\n    HERO STATS    ")
        for stat, value in self.__dict__.items():
            print(f"{stat}: {value}")

class Item:
    def __init__(self, name, effect, item_type):
        self.name = name
        self.effect = effect
        self.type = item_type

    def __str__(self):
        return f"{self.name} (+{self.effect} {self.type})"
    
    def __repr__(self):
        return self.__str__()
    
class Game:
    def __init__(self):
        name = input("What would you like to name your beautiful adventurer? Don't worry about your choice, it can be changed later.")
        self.hero = Hero(name)
        self.running = True

    def stat_decay(self):
        self.hero.hunger -= random.randint(1, 5)
        self.hero.thirst -= random.randint(1, 5)
        self.hero.sleep -= random.randint(1, 3)

        if self.hero.hunger <= 0:
            self.hero.health -= random.randint(5,10)