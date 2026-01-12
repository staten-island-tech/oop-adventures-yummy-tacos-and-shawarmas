def food(self):
    print(f"Food given to {self.name}")
    print(self.name, "starts eating")
    self._change_hunger(30)

def armor(self):
    print(f"Armor given to {self.name}")
    print(self.name, "is now protected")
    self._change_health(30)
    self._change_stamina(-5)

def water(self):
    print(f"water given to {self.name}")
    print(self.name, "is drinking")
    self._change_thirst(20)

def HealingPotion(self):
    print(f"healing potion given to {self.name}")
    print(self.name, "is now healing")
    self._change_health(30)

def SpeedPotion(self):
    print(f"Speed Potion given to {self.name}")
    print(self.name, "gains a speed boost")
    self._change_speed(25)

def Weights(self):
    print(f"Weights given to {self.name}")
    print(self.name, "Starts lifting")
    self._change__strength(20)

def Sword(self):
    print(f"Sword given to {self.name}")
    print(self.name, "gains a sword")
    self._change_strength(10)
    self._change_damage(30)
