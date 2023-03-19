from math import pi, sin, sqrt

def v(w, m):
    v_max = 2 #Световых года / день
    return v_max * (w / 80) * (200 / m)


def gn(g0, kp):
    return g0 + g0 * kp


def kp(t, oxi):
    return sin((-1 * pi) / 2 + (pi * (t + 0.5 * oxi)) / 40)


def e(t):
    return t * (t + 1) / 2


def t(e):
    return (sqrt(1 + 8 * e) - 1) / 2

