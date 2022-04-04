def Substitution(state, sbox_a, sbox_b):
    s = list(state)
    for i in range(0, 6):
        current_a = sbox_a[int(''.join(state[4 * i: 4 * i + 4]), 2)]
        for j in range(0, 4):
            s[4 * i + j] = bin(current_a)[2:].zfill(4)[j]
        current_b = sbox_b[int(''.join(state[24 + 4 * i: 27 + 4 * i]), 2)]
        for j in range(0, 4):
            s[24 + 4 * i + j] = bin(current_b)[2:].zfill(4)[j]
        return ''.join(s)