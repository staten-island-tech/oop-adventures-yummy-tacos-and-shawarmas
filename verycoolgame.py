def food(self):
    print(f"Food given to {self.name}")
    if self.__hunger < 4:
        print(self.name, "starts eating")
        self._change_hunger(2)
    elif self.__hunger < 7:
        print(self.name, "starts eating")
        self._change_hunger(3)
        self._change_thirst(-1)
    else:
        print(self.name, "starts eating")
        self._change_hunger(4)
        self._change_thirst(-2)

def armor(self):
    print(f"Armor given to {self.name}")
    if self.__health < 4:
        print(self.name, "is now protected")
        self._change_health(3)
        self._change_stamina(-1)
    elif self.__health < 7:
        print(self.name, "is now Protected")
        self._change_health(4)
        self._change_stamina(-1)
    else:
        print(self.name, "is now Protected")
        self._change_health(5)
        self._change_stamina(-1)

def water(self):
    print(f"water given to {self.name}")
    if self.__thirst < 4:
        print(self.name, "is drinking")
        self._change_thirst(4)
    elif self.__thirst < 7:
        print(self.name, "is drinking")
        self._change_thirst(3)
        self._change_health(1)
    else:
        print(self.name, "is drinking")
        self._change_thirst(4)
        self._change_health(2)

def HealingPotion(self):
    print(f"healing potion given to {self.name}")
    if self.__health < 4:
        print(self.name, "is now healing")
        self._change_health(2)
    elif self.__health < 7:
        print(self.name, "is now healing")
        self._change_health(3)
        self._change_strength(1)
    else:
        print(self.name, "is now healing")
        self._change_health(-4)
        self._change_strength(2)

def SpeedPotion(self):
    print(f"Speed Potion given to {self.name}")
    if self.__speed < 4:
        print(self.name, "gains a speed boost")
        self._change_speed(2)
    elif self.__speed < 7:
        print(self.name, "gains a speed boost")
        self._change_speed(3)
    else:
        print(self.name, "gains a speed boost")
        self._change_speed(4)

def Weights(self):
    print(f"Weights given to {self.name}")
    if self.__strength < 4:
        print(self.name, "Starts lifting")
        self._change__strength(-2)
    elif self.__strength < 7:
        print(self.name, "Starts lifting")
        self._change_strength(-3)
        self._change_stamina(-1)
    else:
        print(self.name, "Starts lifting")
        self._change_strength(-4)
        self._change_stamina(-2)

def Sword(self):
    print(f"Sword given to {self.name}")
    if self.__strength < 4:
        print(self.name, "gains a sword")
        self._change_strength(3)
        self._change_damage(-1)
    elif self.__strength < 7:
        print(self.name, "gains a sword")
        self._change_strength(4)
        self._change_damage(-1)
    else:
        print(self.name, "gains a sword")
        self._change_health(4)
        self._change_damage(-1)