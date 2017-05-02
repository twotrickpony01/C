import string

character_dict  = string.printable #if this is going to be used several times, may as well alloc memory for it
character_dict_length = len(character_dict) #^

def cipher(plain_text, key): #note that any key that's a multiple of 100 will return your plain_text, but without spaces.
    cipher_text = ""
    plainest_text = plain_text.replace(" ", "") #remove spaces -- string.printable doesn't have any to index
    for letter in plainest_text:
        cipher_text += character_dict[(character_dict.index(letter) + key) % character_dict_length] #takes plain_text letter position, adds the key value,
                                                                                                    # mods by the possible characters length, concats to cipher text
    return cipher_text

def decipher(cipher_text, key):
    deciphered_text = ""
    for letter in cipher_text:
        deciphered_text += character_dict[(character_dict.index(letter) - key) % character_dict_length] #takes plain_text letter position, adds the key value,                                                                                            # mods by the possible characters length, concats to cipher text
    return deciphered_text



def tests():
    print cipher("hey my name is Adam, 124!@#$", 100000000000001)
    print decipher(cipher("hey my name is Adam, 124!@#$", 100000000000001), 100000000000001)
    print
    print cipher("hey my name is Adam, 124!@#$", 1)
    print decipher(cipher("hey my name is Adam, 124!@#$", 1), 1)
    print
    print cipher("hey my name is Adam, 124!@#$", 0)
    print decipher(cipher("hey my name is Adam, 124!@#$", 0), 0)
    print
    print cipher("hey my name is Adam, 124!@#$", -1)
    print decipher(cipher("hey my name is Adam, 124!@#$", -1), -1)
    print
    print cipher("hey my name is Adam, 124!@#$", -1000000000001)
    print decipher(cipher("hey my name is Adam, 124!@#$", -1000000000001), -1000000000001)

tests()

