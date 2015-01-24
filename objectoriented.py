class Point():
    ''' Represents a 2d point'''

    def __init__(self):
        '''Initializer for the class, point'''
        self.x = 0
        self.y = 0

    def reset(self):
        ''' Resets the class, Point '''
        x.reset()
        y.reset()

    def __str__(self):
        '''Returns a string'''
        return 'Point:({}, {})'.format(self.x, self.y)

    def __repr__(self):
        '''Returns a string used to recreate object'''
        return 'Point({}, {})'.format(self.x, self.y)

    def __eq__(self, other):
        '''Compares objects'''
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False



