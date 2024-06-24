list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

length = -1

while (length != len(list)):
    length += 1

    if list[length] < 0:
        break
    print(list[length])

