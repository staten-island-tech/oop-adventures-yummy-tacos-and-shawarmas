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
        print("\n>>> HERO STATS <<<")
        for stat, value in self.__dict__.items():
            print(f"{stat}: {value}")

class NPC(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=random.randint(30, 60),
            stamina=50,
            strength=random.randint(1, 4),
            speed=7,
            damage=random.randint(1, 5)
        )

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
        self.hero.hunger = max(0, self.hero.hunger - random.randint(1, 3))
        self.hero.thirst = max(0, self.hero.thirst - random.randint(1, 3))
        self.hero.sleep = max(0, self.hero.sleep - random.randint(1, 3))

        if self.hero.hunger == 0:
            self.hero.health -= random.randint(5,10)
            print(f"You are starving! Please eat something or your health will decrease.")

        if self.hero.thirst == 0:
            self.hero.health -= random.randint(5,10)
            print(f"You are dehydrated! Please drink something or your health will decrease.")

        if self.hero.sleep == 0:
            self.hero.health -= random.randint(5,10)
            print(f"You are extremely tired! Please rest or your health will decrease.")
    
    def health_regen(self):
        if self.hero.hunger >= 60 and self.hero.thirst >= 60 and self.hero.sleep >= 60 and self.hero.health <= 97:
            self.hero.health += 3
    
        
    def fight(self):
        enemy = NPC("Wild Boar")
        print(f"\nA {enemy.name} appears!")

        while enemy.is_alive() and self.hero.is_alive():
            enemy.health -= self.hero.damage
            self.hero.health -= enemy.damage

        if self.hero.is_alive():
            reward = random.randint(20, 30)
            self.hero.money += reward
            print(f"You defeated the {enemy.name} and earned ${reward}!")
        else:
            print(f"You were defeated by the {enemy}. GAME OVER!")
            self.running = False

    def find_item(self):
        food1 = Item("Apple", 20, "food")
        food2 = Item("Dung", -5, "food")
        food3 = Item("Wild Berry", 10, "food")
        food4 = Item("Mushroom", 30, "food")
        food5 = Item("Durian", 25, "food")
        drink1 = Item("River Water", 30, "drink")
        drink2 = Item("Rain Water", 20, "drink")
        drink3 = Item("Fruit Juice", 25, "drink")
        drink4 = Item("Blood", 1, "drink")
        drink5 = Item("Smoothie", 30, "drink")
        found = random.choice([food1, food2, food3, food4, food5, drink1, drink2, drink3, drink4, drink5])
        self.hero.inventory.append(found)
        print(f"You found a {found.name}!")

    def use_item(self):
        if not self.hero.inventory:
            print("Your inventory is empty.")
            return

        for i, item in enumerate(self.hero.inventory):
            print(f"{i + 1}. {item.name}")

        choice = input("Choose an item to use: ")

        if not choice.isdigit():
            print("Invalid choice.")
            return

        choice = int(choice) - 1

        if choice < 0 or choice >= len(self.hero.inventory):
            print("Invalid choice.")
            return

        item = self.hero.inventory.pop(choice)

        if item.type == "food":
            self.hero.eat(item)
        elif item.type == "drink":
            self.hero.drink(item)
    
    def rest(self):
        if self.hero.sleep >= 90 and self.hero.sleep <= 100:
            self.hero.sleep += 2
            print("You took a very short nap. You only restored 2 sleep since you were already very energized.")
        if self.hero.sleep >= 50 and self.hero.sleep <= 89:
            self.hero.sleep += 5
            print("You took a longer nap to really rest your head. You restore 5 sleep and feel a lot better.")
        if self.hero.sleep >= 25 and self.hero.sleep <= 49:
            self.hero.sleep += 10
            print("You took half the day off and went to sleep. You restore 10 sleep and feel very good.")
        if self.hero.sleep >= 10 and self.hero.sleep <= 24:
            self.hero.sleep += 20
            print("You took the whole day off and had very proper rest. You restore 20 sleep and are ready for the day.")
        if self.hero.sleep >= 0 and self.hero.sleep <= 9:
            self.hero.sleep += 30
            print("You take multiple days off to really fix your sleep schedule. You restore 30 sleep and have fixed your horrible schedule.")

    def game_loop(self):
        while self.running and self.hero.is_alive():
            self.stat_decay()
            self.health_regen()
            self.hero.show_stats()
        
            print("\nChoose an action:")
            print("1) Fight Monster")
            print("2) Scavenge")
            print("3) Use Item")
            print("4) Rest")
            print("5) QUIT GAME")

            choice = input("> ")

            if choice == "1":
                self.fight()
            elif choice == "2":
                self.find_item()
            elif choice == "3":
                self.use_item()
            elif choice == "4":
                self.rest()
            elif choice == "5":
                print("Thanks for playing!")
                self.running = False
            else:
                print("Invalid choice.")

        print(f"You collapsed and died. GAME OVER! Your final stats are:{self.hero.show_stats()}")
        print(self.hero.show_stats())


if __name__ == "__main__":
    game = Game()
    game.game_loop()