class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self, name, energy):
        self.energy += 25
        return self

    def eat(self, name, health, energy):
        self.health += 10
        self.energy += 5
        return self

    def play(self, name, health):
        self.health += 5
        return self

    def noise(self,type):
        if self.type == "dog":
            print("Woof!")
        elif self.type == "cat":
            print("Meow!")
        else:
            print("What am I?!")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
         self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

Nezuko = Pet("Nezuko", "cat", "Epic Defend", 100, 100)
Tanjiro = Ninja("Tanjiro", "Kamado", "sweets", "veggies", Nezuko)

Tanjiro.walk()