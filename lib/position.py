import math

class Position:
    def __init__(self, x = 0.0, y = 0.0, heading = 0.0):
        self.x = x
        self.y = y
        self.heading = heading
    
    def equals(self, position: "Position"):
        return self.x == position.x and self.y == position.y

    def distanceTo(self, position: "Position"):
        if self.equals(position):
            return 0
        return math.dist([self.x, self.y], [position.x, position.y])
    
    def _targetDistrictOffset(self, position: "Position") -> int:
        if position.x > self.x and position.y > self.y:
            offset = 0
        elif position.x >= self.x and position.y <= self.y:
            offset = 90
        elif position.x < self.x and position.y < self.y:
            offset = -180
        else:
            offset = -90

        return offset

    def headingTo(self, position: "Position"):
        if self.equals(position):
            return 0
        
        temp = Position(self.x, position.y) # Temporäre Position bei x(current), y(target) 
        #if self.equals(temp):
        #    temp = Position(position.x, self.y)
        gk = self.distanceTo(temp) # Gegenkathete
        hypo = self.distanceTo(position=position) # Hypothenuse

        bogen = math.asin(gk / hypo) # Winkel in Bogenmaß
        grad = round((bogen / (2 * math.pi)) * 360) # Bogen zu Gradmaß
        offset = self._targetDistrictOffset(position)
        
        if offset == 0 or offset == -180:
            grad = abs(grad-90)
        
        return offset + grad

    
