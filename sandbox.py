def multiplicative_inverse(e: int, phi: int) -> int:

    a, b = e, phi

    l = [[a, b, a % b, a // b, None, None]]

    while a % b != 0:
        a, b = b, a % b
        l.append([a, b, a % b, a // b, None, None])

    l[-1][4], l[-1][5] = 0, 1

    for i in range(len(l) - 2, -1,-1):
        l[i][4] = l[i + 1][5]  # x_i = y_(i+1)
        l[i][5] = l[i + 1][4] - l[i + 1][5] * l[i][3]  # y_i = x_(i+1) - y_(i+1) * (a // b)_i

    return l[0]