'''
Implementation of bridge pattern
'''

class Hero:
    '''
        Class hero behaves like a client of bridge
    '''
    def __init__(self, name, x, y, move_api):
        '''(str, float, float, MoveApi)->None
        Constructor

        Parameters:
            name: hero's name.
            x: x coordinate of start point
            y: y coordinate of start point
            move_api: a concrete implementation of movement api
        Returns:
        '''
        self._name = name
        self._x = x
        self._y = y
        self._move_api = move_api

    def move(self):
        '''()->None
        Move hero from one location to another
        '''
        offset = self._move_api.move_hero()
        self._x += offset[0]
        self._y += offset[1]

    def __repr__(self):
        '''()->None
        Official object representation
        '''
        return "{0}'s current location is {1}:".format(self._name, (self._x, self._y,))

class MoveApi:
    '''
        Abstract implementation of movement
    '''
    pass

class FastMoveApi(MoveApi):
    '''
        Fast movement implementation
    '''
    def move_hero(self):
        '''()->tuple
            Calculate offset from the current location to a new one
        '''
        return (100, 0)

class SlowMoveApi(MoveApi):
    '''
        Slow movement implementation
    '''
    def move_hero(self):
        '''()->tuple
            Calculate offset from the current location to a new one
        '''
        return (20, 0)

if __name__ == "__main__":
    fast_hero = Hero("Sprinter", 0, 0, FastMoveApi())
    slow_hero = Hero("Tortoise", 0, 0, SlowMoveApi())

    for i in range(5):
        fast_hero.move()
        slow_hero.move()
        print(fast_hero)
        print(slow_hero)
    '''
        Output
        Sprinter's current location is (100, 0):
        Tortoise's current location is (20, 0):
        Sprinter's current location is (200, 0):
        Tortoise's current location is (40, 0):
        Sprinter's current location is (300, 0):
        Tortoise's current location is (60, 0):
        Sprinter's current location is (400, 0):
        Tortoise's current location is (80, 0):
        Sprinter's current location is (500, 0):
        Tortoise's current location is (100, 0):
    '''
