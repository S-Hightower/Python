from classes.ninja import Ninja
from classes.pirate import Pirate
import random

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")


def randomAtk():
    attack_roll = random.randint(1,3)
    return attack_roll


while jack_sparrow.health > 0 and michelangelo.health > 0:
    
    attack = randomAtk()
    if attack == 1:
        michelangelo.punch(jack_sparrow)
        print("YOU PUNCHED")
        jack_sparrow.show_stats()
    elif attack == 2:
        michelangelo.nunchuckAtk(jack_sparrow)
        print("YOU NUNCHUCKED")
        jack_sparrow.show_stats()
    elif attack == 3:
        michelangelo.kick(jack_sparrow)
        print("YOU KICKED")
        jack_sparrow.show_stats()
    
    if jack_sparrow.health > 0 and michelangelo.health > 0:
        attack = randomAtk() 
        if attack == 1:
            jack_sparrow.punch(michelangelo)
            print("YOU PUNCHED")
            michelangelo.show_stats()
        elif attack == 2:
            jack_sparrow.swordAtk(michelangelo)
            print("YOU SWORDED")
            michelangelo.show_stats()
        elif attack == 3:
            jack_sparrow.shoot(michelangelo)
            print("YOU SHOOTED")
            michelangelo.show_stats()   

if michelangelo.health <= 0:
    print("*****FATALITY*****\nJACK SPARROW WINS")
else:
    print("*****FATALITY*****\nMICHELANGELO WINS")





############ pick random int 1-3
############ 1) punch
############ 2) nunchucks   
############ 3) kick


