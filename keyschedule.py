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

def AddRoundKey(S,Kr):
    return bin(int(S)^int(Kr))[2:]

def Braiding(B1,B2,B3):
    for i in range(8):
        B3[2*i] = str(int(B3[2*i],2) ^ int(B2[23 - 2*i],2))
        B3[2*i + 1] = str(int(B3[2*i + 1],2) ^ int(B1[2*i+1],2))
        k = B3[2*i] 
        B3[2*i] = B3[2*i + 1]
        B3[2*i + 1] = k
        k = B3[2*i + 1]
        B3[2*i + 1] = B1[2*i+1]
        B1[2*i+1] = B3[2*i + 1]
    k = B1
    B1 = B2
    B2 = k
    return B1, B2
