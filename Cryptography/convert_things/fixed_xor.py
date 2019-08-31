from binascii import * 

def bxor(param1, param2):
    return bytes([x ^ y for x,y in zip(param1, param2)])

A = unhexlify('1c0111001f010100061a024b53535009181c')
B = unhexlify('686974207468652062756c6c277320657965')

print(bxor(A, B))

