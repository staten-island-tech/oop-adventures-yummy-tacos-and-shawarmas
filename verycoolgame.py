class Hero:
<<<<<<< HEAD
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
=======
def food(self):
    print(f"Food given to {self.name}")
    if self.__hunger < 4:
        print(self.name, "kinda eating")
        self._change_hunger(-2)
    elif self.__hunger < 7:
        print(self.name, "eating")
        self._change_hunger(-3)
        self._change_thirst(-1)
    else:
        print(self.name, "eatingx2")
        self._change_hunger(-4)
        self._change_thirst(-2)
        
    if self.__hunger < 2:
        print("cant eat much")
    else:
        if self.__hunger > 7:
          print("eat a lot")

def armor(self):
    print(f"Armor given to {self.name}")
    if self.__hunger < 4:
        print(self.name, "Protected")
        self._change_health(-2)
    elif self.__hunger < 7:
        print(self.name, "Protected")
        self._change_health(-3)
        self._change_stamina(1)
    else:
        print(self.name, "Protected")
        self._change_health(-4)
        self._change_stamina(2)
        
    if self.__health < 2:
        print("Already Protected")
    else:
        if self.__health > 7:
          print("eat a lot")

def water(self):
    print(f"water given to {self.name}")
    if self.__hunger < 4:
        print(self.name, "kinda eating")
        self._change_hunger(-2)
    elif self.__hunger < 7:
        print(self.name, "eating")
        self._change_hunger(-3)
        self._change_happiness(1)
    else:
        print(self.name, "eatingx2")
        self._change_hunger(-4)
        self._change_happiness(2)
        
    if self.__hunger < 2:
        print("cant eat much")
    else:
        if self.__hunger > 7:
          print("eat a lot")

def HealingPotion(self):
    print(f"healing potion given to {self.name}")
    if self.__health < 4:
        print(self.name, "healing")
        self._change_health(-2)
    elif self.__hunger < 7:
        print(self.name, "eating")
        self._change_health(-3)
        self._change_happiness(1)
    else:
        print(self.name, "eatingx2")
        self._change_hunger(-4)
        self._change_happiness(2)
        
    if self.__hunger < 2:
        print("cant eat much")
    else:
        if self.__hunger > 7:
          print("eat a lot")

def SpeedPotion(self):
    print(f"Speed Potion given to {self.name}")
    if self.__hunger < 4:
        print(self.name, "kinda eating")
        self._change_hunger(-2)
    elif self.__hunger < 7:
        print(self.name, "eating")
        self._change_hunger(-3)
        self._change_happiness(1)
    else:
        print(self.name, "eatingx2")
        self._change_hunger(-4)
        self._change_happiness(2)
        
    if self.__hunger < 2:
        print("cant eat much")
    else:
        if self.__hunger > 7:
          print("eat a lot")

def Weights(self):
    print(f"Weights given to {self.name}")
    if self.__strength < 4:
        print(self.name, "weights not very effective")
        self._change__strength(-2)
    elif self.__strength < 7:
        print(self.name, "Gets stronger")
        self._change_strength(-3)
        self._change_stamina(-1)
    else:
        print(self.name, "Starts lifting")
        self._change_strength(-4)
        self._change_stamina(-2)
        
    if self.__strength < 2:
        print("Needs to lift more")
    else:
        if self.__strength > 7:
          print("strong enough")
>>>>>>> Shop/Store
