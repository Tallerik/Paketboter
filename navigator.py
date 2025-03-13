from lib.position import Position


class Navigator:
    
    def __init__(self, x = 0.0, y = 0.0):
        self.current = Position(x,y)
        self.target = Position()
        self.action = Action.IDLE
    

    def goto(self, x,y):
        self.target = Position(x,y)
        self.action = Action.GOTO

        distance = self.current.distanceTo(self.target)
        
        



class Action:
    IDLE = 0
    GOTO = 1