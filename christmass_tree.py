import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

import turtle

# def star():
#     star_size = 100
#     turtle.color("yellow")
#     turtle.fillcolor("yellow")
#     turtle.begin_fill()
#     turtle.width(4)
#     star_angle = 120
#
#     for side in range(5):
#         turtle.forward(star_size)
#         turtle.right(star_angle)
#         turtle.forward(star_size)
#         turtle.right(72 - star_angle)
#s
#     print(turtle.end_fill())


def star_2():
    star = [
        "*",
        (3 * "*"),
        (15 * "*"),
        (9 * "*"),
        (3 * "*" + 5 * " " + 3 * "*"),
        ("*" + 12 * " " + "*")
    ]

    for item in star:
        print((Fore.YELLOW + item).center(44))

star_2()


def tree():
    count = 0
    trunk = 0
    width_extra = 0
    while count != 3:
        height = 0
        width = ""
        width_add = 1
        while height != 5:
            width += width_add * "^" + width_extra * "^"
            print(Fore.GREEN + (width.center(40)))
            width_add += 1
            height += 1
        count += 1
        width_extra += 2
    while trunk != 4:
        print(Fore.MAGENTA + (4 * "|").center(40))
        trunk += 1

tree()