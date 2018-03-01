import random
import math

class warrior:
    def __init__(self,name="Warrior",health=0,attackm =0,blockm =0):
        self.name = name
        self.health = health
        self.attackm = attackm
        self.blockm = blockm

    def attack(self):
         attackm = self.attackm*(random.random()+0.5)
         return attackm
    def block(self):
         blockm = self.blockm*(random.random()+0.5)
         return blockm

class battle:
    def startf(self,warrior1,warrior2):
        while True :
            if self.getattackresult(warrior1,warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getattackresult(warrior2,warrior1) == "Game Over":
                print("Game Over")
                break
    @staticmethod                
    def getattackresult(warriorA,warriorB):
        warriorAattackamt =  warriorA.attack()
        warriorBblockamt = warriorB.block()
        damazewarB = math.ceil(warriorAattackamt- warriorBblockamt)
        warriorB.health = warriorB.health-damazewarB

        print("{} attacks {} and deals {} damage ".format(warriorA.name,warriorB.name,damazewarB))
        print("{} is down to {} health ".format(warriorB.name,warriorB.health ))
        if warriorB.health <=0:
            print("{} has died and {} is victorius ".format(warriorB.name,warriorA.name))
            return "Game Over"
        else:
            return "Fight again"

def main():
    maximus = warrior("maximus",50,20,10)
    naveen = warrior("naveen",50,20,10)
    bttle = battle()
    bttle.startf(maximus,naveen)

main()
    
                  
   
