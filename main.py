import random
import konna
import math
from graphics import Point
import os

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

    return int(math.hypot(pos_y_delta, pos_y_delta))

def listasta(lista, indeksi):
    return [lista[indeksi - 1], lista[indeksi], lista[(indeksi + 1) % len(lista)]]

def saaKulma(oikea_piste, kärkipiste, vasen_piste):
    A = etäisyysNäytöllä(oikea_piste, kärkipiste)
    B = etäisyysNäytöllä(vasen_piste, kärkipiste)
    C = etäisyysNäytöllä(oikea_piste, vasen_piste)

    kulma = math.degrees(math.acos((A * A + B * B - C * C)/(2.0 * A * B)))
    return kulma


kulmien_määrä = 15

kulmien_summa = (kulmien_määrä - 2) * 180

sivut = [i * 5 for i in range(kulmien_määrä - 1, 2 * kulmien_määrä - 1)]

print(sivut)

konna = konna.Konna(window_dim_x=1000, window_dim_y=1000, framerate=3, no_bounds=True)
# konna.penDown()

# angle = random.randint(sisäkulma - sisäkulma / 2, siskulma + sisäkulma / 2)

edelliset = [(0, 0), (0, 10)]

total = 360

sisäkulma = kulmien_summa / kulmien_määrä

counter = 0
kerroin = 1

konna.penDown()
































konna.penUp()
konna.goTo(-250, 0)
konna.penDown()

while True:
    sivu = sivut[random.randint(0, len(sivut) - 1)]
    käännettävä = 180 - sisäkulma - (sivu ** 1.1 / (5 * kulmien_määrä))

    print(sivu, etäisyysNäytöllä((0, 0), konna.dryRun(käännettävä, sivu)), sum(sivut), sivut, etäisyysNäytöllä((0, 0), (konna.pos_x, konna.pos_y)))

    # if etäisyysNäytöllä((0, 0), konna.dryRun(käännettävä, sivu)) <= sum(sivut):
    konna.orientation = konna.orientation + käännettävä
    konna.move(sivu)
    sivut.remove(sivu)







    if len(sivut) == 1:
        konna.goTo(-250, 0)
        break
