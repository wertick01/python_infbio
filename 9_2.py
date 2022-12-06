import numpy as np

class Person(object):

    def __init__(self, name, attack, health, speed, defense, agility, critical_chance):
        self.name = name
        self.health = health
        self.attack = attack
        self.speed = speed
        self.defence = defense
        self.agility = agility
        self.critical_chance = critical_chance
        
    def defend(self):
        probabilty_add_attack = self.critical_chance
        add_attack = np.random.choice([0, 1], p = [1- probabilty_add_attack, probabilty_add_attack])
        if add_attack:
            attack_value = self.attack * 2
        else:
            attack_value = self.attack
        return attack_value

    def protect(self, striker):
        probabilty_add_defense = self.agility
        add_defence = np.random.choice([0, 1], p = [1 - probabilty_add_defense, probabilty_add_defense])
        if add_defence:
            self.health = self.health
        else:
            delta = self.defence - striker.defend()
            if delta < 0:
                self.health = self.health + delta

def battle(first_playser, second_player):
    for _ in range(10000):
        second_player.protect(first_playser)
    if second_player.health <= 0:
        return (first_playser.name)
    first_playser.protect(second_player)
    if first_playser.health <= 0:
        return (second_player.name)

