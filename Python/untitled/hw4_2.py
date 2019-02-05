class Point():
    def __init__(self, xdim = 0, ydim = 0):
        self.xdim = xdim
        self.ydim = ydim

    def __lt__(self,other):

        if self.xdim == other.xdim:
            if self.ydim < other.ydim:
                return True
            if self.ydim >= other.ydim:
                return False
        elif self.xdim < other.xdim:
            return True

        else:
            return False
    def __eq__(self,other):
        if (self.xdim == other.xdim) and (self.ydim == other.ydim):
            return True
        else:
            return False
    def __le__(self, other):
        if (self.xdim == other.xdim) and (self.ydim < other.ydim):
            return True
        elif(self.ydim == other.ydim) and (self.ydim < other.ydim):
            return True
        elif (self.xdim == other.xdim) and (self.ydim == other.ydim):
            return True
        else:
            return False
    def __ne__(self,other):
        if (self.xdim != other.xdim) or (self.ydim != other.ydim):
            return True
        return False
    def __gt__(self, other):
        if (self.xdim > other.xdim):
            return True
        elif (self.xdim == other.xdim) and (self.ydim > other.ydim):
            return True
        else:
            return False
    def __ge__(self, other):
        if (self.xdim == other.xdim) and (self.ydim == other.ydim):
            return True
        elif(self.xdim == other.xdim) and(self.ydim > other.ydim):
            return True
        else:
            return False
    def __add__(self, other):

        return (self.xdim +other.xdim,self.ydim+other.ydim)


point1 = Point(3,6)
point2 = Point(3,6)

"""
print(point1 < point2 )
print(point1 == point2)
print(point1 <= point2)
print(point1 != point2)
print(point1 > point2)
print(point1 >= point2)
print(point1 + point2)
"""

class Line():
    def __init__(self, slope, y_intercept):

        self.slope = slope
        self.y_intercept = y_intercept

    def project(self,point):
        islem = -((self.slope * point.xdim) + point.ydim - self.y_intercept) / ((self.slope ** 2) + 1)

        x = (islem * (1/self.slope)) + point.xdim
        y = islem + point.ydim

        print(x,y)
        return Point(x,y)



point3 = Point(5,3)
line = Line((3/4),3)
line.project(point3)


