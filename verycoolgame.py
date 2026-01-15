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
    
    def update_combat_stats(self):
        self.damage = 5 + self.strength
        self.speed = 5 + (self.stamina // 20)
    

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, 100, 100, 5, 10, 10)
        self.money = 50
        self.max_health = 100
        self.hunger = 100
        self.thirst = 100
        self.sleep = 100
        self.inventory = []

        self.update_combat_stats()

    def apply_poison(self, chance, source):
        if random.random() < chance:
            self.health -= 20
            print(f"You were poisoned by the {source}! You lose 20 health.")
    
    def eat(self, item):
        self.hunger = min(100, self.hunger + item.effect)
        print(f"You eat {item.name}. Your hunger was restored.")

        if item.name == "Wild Berry":
            self.apply_poison(0.1, "Wild Berry")
        elif item.name == "Mushroom":
            self.apply_poison(0.25, "Mushroom")

    def drink(self, item):
        self.thirst = min(100, self.thirst + item.effect)
        print(f"You drink {item.name}. Your thirst was restored.")

        if item.name == "River Water":
            self.apply_poison(0.5, "River Water")

    def show_stats(self):
        print("\n>>> HERO STATS <<<")
        for stat, value in self.__dict__.items():
            if stat == "inventory":
                print("inventory:")
                if not value:
                    print("  (empty)")
                else:
                    for item in value[:6]:
                        print(f"  - {item.name}")
                    if len(value) > 6:
                        print(f"  ...and {len(value) - 6} more items")
            else:
                print(f"{stat}: {value}")

class NPC(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=random.randint(20, 40),
            stamina=40,
            strength=random.randint(1, 3),
            speed=5,
            damage=random.randint(1, 3)
        )
        
        self.update_combat_stats()

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
        if self.hero.hunger >= 50 and self.hero.thirst >= 50 and self.hero.sleep >= 50 and self.hero.health <= 97:
            self.hero.health += 3
    
        
    def fight(self):
        monsters = [
        "Wild Boar",
        "Wolf",
        "Goblin",
        "Bandit",
        "Giant Spider"
    ]

        enemy = NPC(random.choice(monsters))
        print(f"\nA {enemy.name} appears!")

        while enemy.is_alive() and self.hero.is_alive():
            enemy.health -= self.hero.damage
            self.hero.health -= enemy.damage

        if self.hero.is_alive():
            reward = random.randint(20, 30)
            self.hero.money += reward
            print(f"You defeated the {enemy.name} and earned ${reward}!")
        else:
            print(f"You were defeated by the {enemy.name}. GAME OVER!")
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

    def open_inventory(self):
        if not self.hero.inventory:
            print("\nYour inventory is empty.")
            return

        print("\n>>> INVENTORY <<<")

        for i, item in enumerate(self.hero.inventory):
            print(f"\n{i + 1}. {item.name}")
            print(f"   Type: {item.type}")
            print(f"   Stat Gain: +{item.effect}")

            if item.name == "Wild Berry":
                print("   Effect: 10% chance to poison (-20 health)")
            elif item.name == "Mushroom":
                print("   Effect: 25% chance to poison (-20 health)")
            elif item.name == "River Water":
                print("   Effect: 50% chance to poison (-20 health)")
            elif item.name == "Dung":
                print("   Effect: Disgusting. Lowers hunger.")
            elif item.name == "Blood":
                print("   Effect: Why? Gives thirst, but at what cost?")
            else:
                print("   Effect: None")

    def use_item(self):
        if not self.hero.inventory:
            print("Your inventory is empty.")
            return

        print("\n>>> USE ITEM <<<")

        for i, item in enumerate(self.hero.inventory):
            sign = "+" if item.effect >= 0 else ""
            print(f"{i + 1}. {item.name} ({item.type}, {sign}{item.effect})")

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
    
    def go_to_gym(self):
        print("\n WELCOME TO THE DIAMOND GYM ")
        print("1) Dumbbells (+2 Strength, -10 Stamina)")
        print("2) Treadmill (+15 Stamina)")
        print("3) Barbell (+3 Strength, -15 Stamina)")
        print("4) Exit Gym")

        choice = input("> ")

        if choice == "1" and self.hero.stamina >= 10:
            self.hero.strength += 2
            self.hero.stamina -= 10
            print("You lift dumbbells. Strength increased!")

        elif choice == "2":
            self.hero.stamina = min(100, self.hero.stamina + 15)
            print("You run on the treadmill. Stamina increased!")

        elif choice == "3" and self.hero.stamina >= 15:
            self.hero.strength += 3
            self.hero.stamina -= 15
            print("You lift the barbell. Strength increased significantly!")

        elif choice == "4":
            return
        else:
            print("You are too tired or made an invalid choice.")
            return

        self.hero.update_combat_stats()

    def walk_forward(self):
        print("\nYou walk forward...")

        roll = random.random()

        if roll < 0.25:
            monsters = ["Wolf", "Goblin", "Bandit", "Giant Spider", "Wild Boar"]
            enemy = NPC(random.choice(monsters))
            print(f"A {enemy.name} attacks!")

            dodge_chance = min(0.5, self.hero.speed * 0.03)

            if random.random() < dodge_chance:
                print("You dodge the attack because you are too fast!")
                return

            print("You fail to dodge and must fight!")

            while enemy.is_alive() and self.hero.is_alive():
                enemy.health -= self.hero.damage
                self.hero.health -= enemy.damage

        elif roll < 0.35:
            print("You find a chest.")
            if random.random() < 0.75:
                print("The chest is empty.")
            else:
                potion = random.choice(["strength", "stamina", "health"])
                if potion == "strength":
                    self.hero.strength += 10
                    print("Potion of Strength! +10 Strength")
                elif potion == "stamina":
                    self.hero.stamina = min(100, self.hero.stamina + 50)
                    print("Potion of Endurance! +50 Stamina")
                else:
                    self.hero.max_health += 10
                    self.hero.health += 10
                    print("Potion of Vitality! +10 Max Health")

                self.hero.update_combat_stats()
        else:
            print("Nothing happens.")
    
    def discard_item(self):
        if not self.hero.inventory:
            print("Your inventory is empty. Nothing to discard.")
            return

        print("\nChoose an item to discard:")

        for i, item in enumerate(self.hero.inventory):
            print(f"{i + 1}. {item.name}")

        choice = input("> ")

        if not choice.isdigit():
            print("Invalid choice.")
            return

        choice = int(choice) - 1

        if choice < 0 or choice >= len(self.hero.inventory):
            print("Invalid choice.")
            return

        removed_item = self.hero.inventory.pop(choice)
        print(f"You discarded {removed_item.name}.")

    def game_loop(self):
        while self.running and self.hero.is_alive():
            self.stat_decay()
            self.health_regen()
            self.hero.show_stats()
        
            print("\nChoose an action:")
            print("1) Fight Monster")
            print("2) Scavenge")
            print("3) Open Inventory")
            print("4) Use Item")
            print("5) Discard Item")
            print("6) Rest")
            print("7) Go to Gym")
            print("8) Walk Forward")
            print("9) QUIT GAME")

            choice = input("> ")

            if choice == "1":
                self.fight()
            elif choice == "2":
                self.find_item()
            elif choice == "3":
                self.open_inventory()
            elif choice =="4":
                self.use_item()
            elif choice == "5":
                self.discard_item()
            elif choice == "6":
                self.rest()
            elif choice == "7":
                self.go_to_gym()
            elif choice == "8":
                self.walk_forward()
            elif choice == "9":
                print("Thanks for playing!")
                self.running = False
            else:
                print("Invalid choice.")

        print("\nYou collapsed and died. GAME OVER! Your final stats were:")
        self.hero.show_stats()


if __name__ == "__main__":
    game = Game()
    game.game_loop()