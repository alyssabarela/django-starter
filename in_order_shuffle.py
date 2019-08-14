def is_in_order_shuffle(x, y, z):
    if len(z) != len(x) + len(y):
        return False
    for character in x:
        if character not in z:
            return False
    for character in y:
        if character not in z:
            return False

    def recursive_in_order_shuffle(x, y, z):
        if x == "" and y == "" and z == "":
            return True
        if (x and z[0] == x[0]) or y and z[0] == y[0]:
            if x and z[0] == x[0] and y and z[0] == y[0]:
                z = z[1:]
                temp_x = x[1:]
                temp_y = y[1:]
                return recursive_in_order_shuffle(temp_x, y, z) or recursive_in_order_shuffle(x, temp_y, z)
            if x and z[0] == x[0]:
                z = z[1:]
                x = x[1:]
                return recursive_in_order_shuffle(x, y, z)
            if y and z[0] == y[0]:
                z = z[1:]
                y = y[1:]
                return recursive_in_order_shuffle(x, y, z)
        else:
            return False

    return recursive_in_order_shuffle(x, y, z)


x = "abcc"
y = "aa"
z = "aabcac"
print(is_in_order_shuffle(x, y, z))
