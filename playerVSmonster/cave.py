from location import Location
from player import Player
from monster import Monster
from weapon import Weapon
import math
import random

class Cave(Location):

    def __init__(self, name, message):
        super().__init__(name, message)

    def Fight(self, player:Player, monster:Monster, weapon:Weapon):
        print(f"Peleando con el monstruo {monster}")
        if self.attack(player, monster, weapon):
            print("Venciste al monstruo. Felicitaciones!!!")
            player.add_defeated_monster(monster)
            print("Se agrego el montruo a la lista de monstruos vencidos.")
            self.defeat_monster(player, monster)
        else:
            print(":( Perdiste!!!")


    def Exit(self):
        super().Exit()

    def __str__(self):
        return f"{self._message}"
    

    def isMonsterHit(self, player:Player):
        if random.random() > 0.2 or player.get_health() < 20:
            return True
        return False
    

    def attack(self, player:Player, monster:Monster, weapon:Weapon):
        banTerminar = False
        gano = False
        while True:
            health = player.get_health() - monster.getMonsterAttackValue(player.get_xp())
            player.set_health(health)
            if self.isMonsterHit(player):
                monster.set_health(weapon.get_power() + math.floor(random.random() * player.get_xp() + 1))
            else:
                print("Erraste.")
            
            
            if (player.get_health() <= 0):
                player.set_health(0)
                banTerminar = True
                
            elif (monster.get_health() <= 0):
                banTerminar = True
                gano = True
                
            
            if random.random() <= 0.1 and len(player.GetWeapon()) != 1 :
                print("Tu arma se rompió")
                player.remove_weapon(weapon)

            if banTerminar == True:
                break
            
        
        return gano
   
   
    def defeat_monster(self, player:Player, monster:Monster):
        gold = math.floor(monster.get_level() * 6.7)
        gold += player.get_gold()
        player.set_gold(gold)
        xp = monster.get_level()
        xp += player.get_xp()
        player.set_xp(xp)

