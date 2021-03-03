import random


class Unit:

    def __init__(self, name, clan, health=100, strength=10, agility=10, intelligence=10):
        self.name = name
        self.clan = clan
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def _health(self):
        self.health = random.randint(1, 100)
        return self.health

    def _strength(self):
        self.strength = random.randint(1, 10)
        return self.strength

    def _agility(self):
        self.agility = random.randint(1, 10)
        return self.agility

    def _intelligence(self):
        self.intelligence = random.randint(1, 10)
        return self.intelligence

    def healing(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        return self.health


class Mage(Unit):

    def __init__(self, name, clan, magic_type):
        super().__init__(name, clan)
        self.magic_type = magic_type
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intelligence = self._intelligence()

    def inc_intelligence(self):
        if self.intelligence <= 9:
            self.intelligence += 1
        else:
            self.intelligence = 10
        return self.intelligence


mage = Mage('Funtik', 'Aliens', 'Fire')
print(f'{mage.name} is the Mage from {mage.clan} clan. He is armed with a {mage.magic_type} magic. Health: {mage.health}. Strength: {mage.strength}. Agility: {mage.agility}. Intelligence: {mage.intelligence}.')
print(f'{mage.name} increase his health to {mage.healing()}% and intelligence to {mage.inc_intelligence()} points.')
print('___________________________________________')


class Archer(Unit):

    def __init__(self, name, clan, bow_type):
        super().__init__(name, clan)
        self.bow_type = bow_type
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intelligence = self._intelligence()

    def inc_agility(self):
        if self.agility <= 9:
            self.agility += 1
        else:
            self.agility = 10
        return self.agility


archer = Archer('Luntik', 'Turtle', 'Сrossbow')
print(f'{archer.name} is the Archer from {archer.clan} clan. He is armed with a {archer.bow_type}. Health: {archer.health}. Strength: {archer.strength}. Agility: {archer.agility}. Intelligence: {archer.intelligence}.')
print(f'{archer.name} increase his health to {archer.healing()}% and agility to {archer.inc_agility()} points.')
print('___________________________________________')


class Knight(Unit):

    def __init__(self, name, clan, arms_type):
        super().__init__(name, clan)
        self.arms_type = arms_type
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intelligence = self._intelligence()

    def inc_strength(self):
        if self.strength <= 9:
            self.strength += 1
        else:
            self.strength = 10
        return self.strength


knight = Knight('Runtik', 'Wolfes', 'Sword')
print(f'{knight.name} is the Knight from {knight.clan} clan. He is armed with a {knight.arms_type}. Health: {knight.health}. Strength: {knight.strength}. Agility: {knight.agility}. Intelligence: {knight.intelligence}.')
print(f'{knight.name} increase his health to {knight.healing()}% and strength to {knight.inc_strength()} points.')
print('___________________________________________')