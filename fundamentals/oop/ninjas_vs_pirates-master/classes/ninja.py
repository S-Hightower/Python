class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.nunchucks = 15
    
    def show_stats( self ):
        print(f"Name: {self.name}\nHealth: {self.health}\n")

    def punch( self , pirate ):
        pirate.health -= self.strength
        return self

    def nunchuckAtk(self, pirate):
        pirate.health -= (self.strength + self. nunchucks)
        return self
    
    def kick(self, pirate):
        pirate.health -= self.strength * 2
        return self