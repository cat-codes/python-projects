def tree():
    line = 0
    layer = ""
    increment = 1
    count = 0
    while count != 3:
        while line != 7:
            increase = (increment * "o")
            layer += increase
            print(layer)
        increment += 1
        count += 1
tree()