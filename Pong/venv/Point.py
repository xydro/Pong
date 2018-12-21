import math


class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def __str__(self): return 'Point(' + str(self.x) + ',' + str(self.y) + ')'

    def __add__(self, other): return Point(self.x + other.x, self.y + other.y)

    def getx(self): return self.__x
    def gety(self): return self.__y

    def setx(self, val): self.__x = val
    def sety(self, val): self.__y = val

    x = property(getx, gety)
    y = property(gety, sety)

    def distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        nx = (self.__x / self.distance())
        ny = (self.__y / self.distance())
        return [nx, ny]
        #self.__x = (self.__x / self.distance())
        #self.__y = (self.__y / self.distance())


    def rotate(self, degree, origin=(0, 0)):
        # Convert the degree to radians
        radians = math.radians(degree)

        # In case there's an origin, adjust
        offset_x, offset_y = origin
        adjusted_x = (self.__x - offset_x)
        adjusted_y = (self.__y - offset_y)
        # Get the cosine of the degree, then the cosine
        # |cos(degree)   sin(degree)
        # |-sin(degree)  cos(degree)
        cos_rad = math.cos(radians)
        sin_rad = math.sin(radians)

        # Use the vector rotation formula to rotate the vector
        # new x = xcos(degree) - ysin(degree)
        # new y = xsin(degree) + ycos(degree)
        rx = offset_x + cos_rad * adjusted_x - sin_rad * adjusted_y
        ry = offset_y + sin_rad * adjusted_x + cos_rad * adjusted_y

        self.__x = rx
        self.__y = ry

    def angle(self):
        rDeg = math.atan2(self.__x, self.__y)
        nAngle = math.degrees(rDeg)
        return nAngle

