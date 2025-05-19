#!/usr/bin/python3

import random

def simulation_pile_face(n):
    i_prev = None
    serie_actu = 0
    serie_max = 0

    piece = {'pile': 0, 'face': 0, 'max_serie': 0}
    resultat = [random.choice(['pile', 'face']) for _ in range(n)]

    piece['pile'] = resultat.count('pile')
    piece['face'] = resultat.count('face')	

    for i in resultat:
        if i == i_prev:
            serie_actu += 1
        else:
            serie_actu = 1
        i_prev = i
        if serie_actu > serie_max:
            serie_max = serie_actu

    piece['max_serie'] = serie_max

    return piece
