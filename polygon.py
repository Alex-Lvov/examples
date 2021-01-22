from turtle import *
from math import *

"""
https://docs.python.org/3/library/turtle.html
https://ru.onlinemschool.com/math/formula/regular_polygon/
http://www.math24.ru/%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA.html
"""


def solve_poligon(n, radius=200, show_info=False):
    a = 2 * radius * sin(radians(180/n))
    r = ( radius**2 - a**2 / 4 )**0.5
    # r = a / (2 * tan(radians(180/n)))

    if show_info:
        poligon_desc = f"""
        {i}-угольник со стороной {b}
        Радиус вписанной окружности: {r}
        Радиус описанной окружности: {r_prev}
        Внутренний угол: {internal_angle(i)}
        Внешний угол: {outside_angle(i)}
            """
        print(poligon_desc)

    return a, r


def internal_angle(n):
    return 180 * (n-2) / n


def outside_angle(n):
    return 360 / n


def poligon(n, radius=200):
    b, r = solve_poligon(i, radius)
    up()
    home()
    dot()
    forward(r)
    left(90)
    forward(b/2)
    down()

    for j in range(i):
        left(outside_angle(i))
        forward(b)
    return r

def circle_at(r):
    up()
    home()
    goto(0, -r)
    down()
    circle(r)
    return r


def recursive_poligon(n, radius=200, show_info=False, stop_at=3):
    radius = radius if radius > 0 else 200
    stop_at = stop_at if stop_at >= 3 else 3

    b, r = solve_poligon(n, radius)
    up()
    home()
    dot()
    forward(r)
    left(90)
    forward(b/2)
    down()

    for i in range(n):
        # print(f"{i+1} from {n}")
        left(outside_angle(n))
        forward(b)

    circle_at(r)

    if n-1 >= stop_at:
        recursive_poligon(n-1, r, stop_at, show_info)

    return r


if __name__ == "__main__":

    from_n = 20
    to_n = 3
    r = 200
    speed(0)
    use_rerecursive = True

    while True:
        if use_rerecursive:
            recursive_poligon(from_n, r, stop_at=to_n)
        else:
            for i in range(from_n, to_n, -1):
                r = circle_at(poligon(i, r))
        resetscreen()

    done()
