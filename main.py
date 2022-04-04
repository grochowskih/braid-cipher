from keyschedule import AddRoundKey, KeySchedule, Braiding
from Substitution import Substitution

s1=[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9]
s2=[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6]
s3=[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14]

def main(k,c):
    rounds=12
    keys=KeySchedule(k)
    for r in range(rounds-1):
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



plaintext= '1'*64
key='1'*48

main(plaintext,key)