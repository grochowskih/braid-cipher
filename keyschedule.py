def key_schedule(key, d):
    keys = [key] + [0]*12
    r = [1]
    for i in range(2, 14):
        r.append(2*r[i-2] ^ int("7d", 16))
        rc = int("".join([bin(r[i-1])[2:]] + ["00"*16]*5), 2)
        keys[i-1] = keys[i-2] ^ (rc >> (2*i))
        for j in range(12):
            keys[4*j : 4*j + 3] = s_box_1(int(keys[4*j : 4*j + 3], 2))
    return keys
