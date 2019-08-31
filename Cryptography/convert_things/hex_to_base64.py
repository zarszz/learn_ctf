import base64

string_from_challenge = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

string_in_hex = string_from_challenge.decode('hex')

print 'String in hex : ', string_in_hex, "\n"

print "Convert String to base64 ...... \n"

string_in_base64 = base64.b64encode(string_in_hex)

print "String in base64 is below .....\n"
print string_in_base64

