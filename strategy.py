'''
    Implementation of strategy pattern
'''

class AttackStrategy:
    '''
        Base class for attack strategy
    '''
    def __init__(self, gun):
        '''(Weapon)->void
            Constructor
        '''
        self.gun = gun

    def do_attack(self):
        '''
            Perform attack

            Raises:
                Exception
        '''
        raise Exception("Should be implemented in subclasses")

class SingleAttack(AttackStrategy):
    def do_attack(self):
        '''
            Perform single attack
        '''
        self.gun.shoot()

class DoubleAttack(AttackStrategy):
    def do_attack(self):
        '''
            Perform double attack by calling gun attack twice
        '''
        self.gun.shoot()
        self.gun.shoot()

class Weapon:
    def shoot(self):
        '''
            Weapon is shooting
        '''
        print("Shooting...")
class Gun(Weapon):
    def shoot(self):
        '''
            Gun is shooting
        '''
        print("Gun is working")

class Creature:
    def __init__(self, name, attack):
        '''(str,AttackStrategy)->void
            Constructor
        '''
        self.name = name
        self.attack = attack

    def do_attack(self):
        '''
            Creature attacks its enemies depending on attack strategy
        '''
        print(self.name)
        self.attack.do_attack()

if __name__ == "__main__":
    gun = Gun()
    single_attack = SingleAttack(gun)
    double_attack = DoubleAttack(gun)

    simple_soldier = Creature("First level soldier", single_attack)
    advanced_soldier = Creature("Advanced level soldier", double_attack)

    simple_soldier.do_attack()
    advanced_soldier.do_attack()