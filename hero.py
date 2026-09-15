import random 

class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = 20    

    def attack(self):
        return random.randint(1,self.attack_power)

    def take_damage(self, damage):
        # Subtract damage, but do not allow health to fall below 0.
        self.health = max(0, self.health - damage)
        print(f"{self.name} receives {damage} damage. Health: {self.health}")

    def is_alive(self):
        if self.health > 0:
            return True
        else: 
            return False