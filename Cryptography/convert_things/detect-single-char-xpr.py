from binascii import *
from os import urandom

ascii_lower_case = [x for x in range(97, 122)] + [32]

#class InvalidMessageException(Exception):
#    pass

def xor_return_bytes(ciphertext, keystream):
    return bytes([x ^ y for x,y in zip(ciphertext, keystream)])

def brute_force_every_byte_xor(ciphertext):
    best = {"nb_letters": 0}

    for i in range(2**8):
        candidate_key = i.to_bytes(1, byteorder='big')
        keystream = candidate_key*len(ciphertext)
        candidate_message = xor_return_bytes(ciphertext, keystream)
        nb_letters = sum([x in ascii_lower_case for x in candidate_message])
        if nb_letters > best['nb_letters']:
            best = {"message": candidate_message, "nb_letters": nb_letters, "key": candidate_key}
    if best['nb_letters'] > 0.7*len(ciphertext):
        return best
   # else:
    #    raise InvalidMessageException('best candidate message is: %s' % best['message'])

with open('data4.txt') as data_file:
    ciphertext_list = [ unhexlify(line.strip()) for line in data_file ]
    candidates = list()

    for (line_nb, ciphertext) in enumerate(ciphertext_list):
        try:
            message = brute_force_every_byte_xor(ciphertext)['message']
        except Exception:
            pass
        else:
            print('append')
            candidates.append({
                'line_nb': line_nb,
                'ciphertext': ciphertext,
                'message': message
                })

    if len(candidates) > 1:
        print("Error: more than one candidate")
    else:
        for (key, value) in candidates[0].items():
            print(f'{key}: {value}')

