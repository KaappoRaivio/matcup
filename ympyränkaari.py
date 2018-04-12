import math
from graphics import *

class InsifficentUnitError(Exception):
    pass

def etäisyysNäytöllä(piste_1, piste_2):
    pos_1_x, pos_1_y, pos_2_x, pos_2_y = 0, 0, 0, 0

    if isinstance(piste_1, Point):
        pos_1_x = piste_1.x
        pos_1_y = piste_1.y
    else:
        pos_1_x = piste_1[0]
        pos_1_y = piste_1[1]

    if isinstance(piste_2, Point):
        pos_2_x = piste_2.x
        pos_2_y = piste_2.y
    else:
        pos_2_x = piste_2[0]
        pos_2_y = piste_2[1]

    pos_x_delta = abs(pos_2_x - pos_1_x)
    pos_y_delta = abs(pos_2_y - pos_1_y)

    return math.sqrt(pos_x_delta ** 2 + pos_y_delta ** 2)

def customRange(start, end, step):
    i = start
    while i < end:
        yield i
        i += step

class Annulus(object):
    __id = 0
    instances = []

    def __str__(self):
        return f'X: {self.pos_x}; Y: {self.pos_y}; radius: {self.radius}'

    def __init__(self, pos_x, pos_y, radius):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.radius = radius

        self.points = [(math.cos(math.radians(i)) * self.radius + self.pos_x, math.sin(math.radians(i)) * self.radius + self.pos_y) for i in customRange(0, 360, 1)]
        # print(self.points)
        # print('moi')

        self.__id = Annulus.__id
        Annulus.__id += 1

        Annulus.instances.append(self)

    def intercept(self, instance):
        points = []
        print('beginnign')

        for index in range(len(instance.points)):
            for index_2 in range(len(self.points)):
                if etäisyysNäytöllä(self.points[index_2], instance.points[index]) < 10:

                    points.append(instance.points[index])
                    # except KeyError:
                    #     points[instance] = [instance.points[index]]
        # quit()
        # print('end')
        print('ned')
        return points

    def jump(self, angle, unit='degrees'):
        if unit.lower() == 'degrees':
            angle = math.radians(angle)
        elif unit.lower() != 'radians':
            raise InsifficentUnitError('Wrong unit!')

        pos_x_delta = self.pos_x + math.sin(angle) * self.radius
        pos_y_delta = self.pos_y + math.cos(angle) * self.radius

        return Point(round(pos_x_delta, 0), round(pos_y_delta, 0))


    def drawPoints(instance, window):
        for i in instance.points:
            temp = Point(*i)
            # temp.x += window.getWidth()
            # temp.y += window.getHeight()
            temp.x += 500
            temp.y += 500
            temp.draw(window)

# a = Annulus(0, 0, 100)
# b = Annulus(0, 50, 100)

# print(a.intercept(b))
