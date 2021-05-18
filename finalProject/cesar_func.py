def crypt(args, x):
    ciphertext = str(args)
    shift = int(x)

    ciphertext = ciphertext.split()


    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o + shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)


    sentence = ' '.join(sentence)
    print('Decryption Successful\n')
    print('Your encrypted sentence is:', sentence)
    return sentence


def decrypt(args, x):
    ciphertext = str(args)
    shift = int(x)


    ciphertext = ciphertext.split()


    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)


    sentence = ' '.join(sentence)
    return sentence


