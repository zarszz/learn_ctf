#! env/bin/python3

from binascii import *

ascii_lower_case = [x for x in range(97, 122)] + [32]

def xor_return_bytes(ciphertext, keystream):
    return bytes([x ^ y for x,y in zip(ciphertext, keystream)])

def brute_force_every_byte_xor(ciphertext):
    best = None

    for i in range(2**8):
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(ciphertext)
        candidate_message = xor_return_bytes(ciphertext, keystream)
        nb_letters = sum([x in ascii_lower_case for x in candidate_message])
        if best is None or nb_letters > best['nb_letters']:
            best = {"message": candidate_message, "nb_letters": nb_letters, "key": candidate_key}
    return best

#result = brute_force_every_byte_xor(unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'))

#print('key : ', result['key'])
#print('message : ', result['message'])
#print('nb of letters : ', result['nb_letters'])
