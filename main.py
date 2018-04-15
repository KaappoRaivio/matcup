

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


konna = konna.Konna(window_dim_x=1920, window_dim_y=1080, framerate=2, no_bounds=True)


konna.penDown()

konna.penUp()
konna.goTo(-250, 0)
konna.penDown()
konna.line_width = 10

input()

while True:

    alkamis_x = random.randint(-konna.window.getWidth() / 2, konna.window.getWidth() / 2)
    print(-konna.window.getWidth() / 2)
    alkamis_y = random.randint(-konna.window.getHeight() / 2, konna.window.getHeight() / 2)


    konna.penUp()
    konna.line_color = ['blue', 'green', 'red', 'yellow', 'orange', 'purple'][random.randint(0, 5)]
    konna.goTo(alkamis_x, alkamis_y)
    konna.penDown()

    kulmien_määrä = random.randint(3, 8)

    kulmien_summa = (kulmien_määrä - 2) * 180

    sisäkulma = kulmien_summa / kulmien_määrä

    sivut = [i * 10 for i in range(kulmien_määrä - 1, 2 * kulmien_määrä - 1)]

    while True:
        sivu = sivut[random.randint(0, len(sivut) - 1)]
        käännettävä = 180 - sisäkulma - (sivu ** 1.1 / (5 * kulmien_määrä))

        if len(sivut) == 2:
            käännettävä += 5

        if len(sivut) == 3:
            käännettävä += 5

        if len(sivut) == 4:
            käännettävä += 5

        konna.orientation = konna.orientation + käännettävä
        konna.move(sivu)
        sivut.remove(sivu)


        if len(sivut) == 1:
            sivut = []
            konna.goTo(alkamis_x, alkamis_y)
            break
