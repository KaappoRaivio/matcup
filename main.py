import konna
import math
from ympyränkaari import *
import random
from graphics import *
import time
import copy

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

def listasta(lista, indeksi):
    return [lista[indeksi - 1], lista[indeksi], lista[(indeksi + 1) % len(lista)]]

def kulma(oikea_piste, kärkipiste, vasen_piste):
    A = etäisyysNäytöllä(oikea_piste, kärkipiste)
    B = etäisyysNäytöllä(vasen_piste, kärkipiste)
    C = etäisyysNäytöllä(oikea_piste, vasen_piste)

    kulma = math.degrees(math.acos((A * A + B * B - C * C)/(2.0 * A * B)))
    return kulma

kulmien_määrä = 10

sivut = [i * 10 for i in range(kulmien_määrä - 1, 2 * kulmien_määrä - 1)]

s = copy.deepcopy(sivut)

a = Annulus(0, 0, sivut.pop(random.randint(0, len(sivut) - 1)))

piste = None

pisteet = [Point(0, 0)]

while sivut:
    indeksi = random.randint(0, len(a.points) - 1)

    piste = Point(*a.points[indeksi])

    try:
        # print(kulma(piste, pisteet[-1], pisteet[-2]))
        if kulma(piste, pisteet[-1], pisteet[-2]) > 180:
            piste = None
    except:
        pass

    if int(etäisyysNäytöllä(piste, (0, 0))) >= sum(sivut):
        piste = None

    if piste is not None:
        pisteet.append(piste)
        a = Annulus(piste.x, piste.y, sivut.pop(random.randint(0, len(sivut) - 1)))

pisteet.append(pisteet[0])

print(etäisyysNäytöllä(pisteet[-1], pisteet[-2]))
print(s)
# quit()

a = GraphWin('Matcup', 1000, 1000)
for i in range(len(pisteet)):
    line = Line(pisteet[i], pisteet[(i + 1) % len(pisteet)])
    line.move(a.getWidth() / 2, a.getHeight() / 2)
    line.draw(a)
    # time.sleep(1)


input()
