import random
class blade():
    def __init__(self, damage, critical,chance):
        self.damage=damage
        self.critial=critical
        self.chance=chance
    def crit_or_not(self):
        arr=list(range(1,101))
        random_value=random.randint(1,100)
        if random_value<=self.chance:
            damage=self.critial*self.damage
            print('выпал крит')
            return damage
        else: 
            damage=self.damage
            return damage

class warrior():
    def __init__(self, name, health, blade):
        self.name=name
        self.health=health
        self.blade=blade
    def Attack(self,warrior:'warrior'):
        warrior.health -= self.blade.crit_or_not()

def battle(warrior1:warrior,warrior2:warrior,blade_warrior1:blade, blade_warrior2:blade):
    while True:
        if warrior1.health<=0:
            print(f'{warrior2.name}, победил')
            break
        warrior1.Attack(warrior2)
        print(f'{warrior1.name}.удар!', warrior1.health)
        if warrior2.health<=0:
            print(f'{warrior1.name}, победил')
            break
        warrior2.Attack(warrior1)
        print(f'{warrior2.name}.удар!', warrior1.health)
frostmorn=blade(10,1.5,20)       
peace_of_shit = blade(10,3,10)
Artes = warrior('Artes',100,frostmorn)
Illidan= warrior('Illidan',100,peace_of_shit)
battle(Artes,Illidan,frostmorn,peace_of_shit)

# def damage(self):
#     print(self.damage())