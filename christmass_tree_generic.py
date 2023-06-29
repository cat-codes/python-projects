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
            print(width.center(40))
            width_add += 1
            height += 1
        count += 1
        width_extra += 2
    while trunk != 4:
        print((4 * "|").center(40))
        trunk += 1
tree()