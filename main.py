
def main(k,c):
    rounds=12
    keys=KeySchedule(k)
    for i in range(rounds-1):
        if r%2 == 1:
            AddRoundKey(c[0:48],k[r])
            Substitution(c[0:48],s1,s2)
            Braiding(c[0:24], c[24:48],c[48:64])
        if r%2 == 0:
            AddRoundKey(c[16:64],k[r])
            Substitution(c[16:64],s2,s3)
            Braiding(c[40:64], c[16:40],c[0:15])
    AddRoundKey(c[16:64],k[12])
    Substitution(c[16:64],s2,s3)
    AddRoundKey(c[16:64],k[13])
    return c[0:64]