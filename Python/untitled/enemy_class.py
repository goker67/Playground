import random

class Enemy:
    def __init__(self, name="Enemy", health=500, attack_power=10, bullet_number=5):
        self.name = name
        self.health = health
        self.attack_power= attack_power
        self.bullet_number= bullet_number

    def print(self):
        print("İsim:",self.name,"Kalan can:",self.health,"Saldırı Gücü:",self.attack_power,"Mermi Sayısı",
              self.bullet_number)

    def attack(self):

        print(self.name + " saldırıyor")
        used_bullet = random.randrange(0,10)
        print(str(used_bullet)+" kadar harcandı")
        self.bullet_number -= used_bullet

        return(used_bullet,self.attack_power)

    def injure(self,used_bullet,attack_power):
        self.health -= (used_bullet * attack_power)
        print(self.name +" :vuruldum")

    def bullet_empty(self):
        if(self.bullet_number <= 0):
            print(self.name+" konuşuyor:Mermim bitti.")
            return True
        return False

    def isalive(self):
        if (self.health <= 0):
            print("Enemy dead")
        else:
            print(str(self.health) + "canım kaldı")




enemies = []

i=0
while (i<10):
    random_health = random.randrange(100,200)
    random_attackPower = random.randrange(10,20)
    random_bulletNumber = random.randrange(20,30)
    newEnemy = Enemy("Enemy" + str(i+1),random_health,random_attackPower,random_bulletNumber)
    enemies.append(newEnemy)

    i +=1

i = 0
while (i<3):
    random_enemy1 = random.randrange(0,10)
    random_enemy2 = random.randrange(0,10)

    returned_value = enemies[random_enemy1].attack() #harcanan mermi 15, saldırı gücü 5 (15,5)
    enemies[random_enemy2].injure(returned_value[0],returned_value[1])
    print("Round bitti")

    i +=1






