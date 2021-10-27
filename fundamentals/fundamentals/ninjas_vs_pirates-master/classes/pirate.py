class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 3
        self.health = 100
        self.sword = 10
        self.gun = 20

    def show_stats( self ):
        print(f"Name: {self.name}\nHealth: {self.health}\n")

    def punch ( self , ninja ):
        ninja.health -= self.strength
        return self

    def swordAtk( self, ninja):
        ninja.health -= self.strength + self.sword
        return self

    def shoot(self , ninja):
        ninja.health -= self.strength + self.gun
        return self