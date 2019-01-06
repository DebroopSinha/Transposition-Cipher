from collections import OrderedDict

def encrypt(message, key):
    old_key = OrderedDict()
    cipher = {}
    kl = 0
    buffer_letters = 'abcdefghijklmnopqrstuvwxyz'

    for i in key:                                      #Finding the order in which key should be arranged for encryption
        cipher[i] = []
        old_key[ord(i)] = i
    new_key = ''.join(OrderedDict(sorted(old_key.items())).values()) #new_key is the rearranged (by ascii values) key

    messagelength = len(message)
    keylength = len(key)

    for letter_index in range(messagelength):          #Encrypt the plaintext message column-wise according to key
        cipher[key[letter_index%keylength]].append(message[letter_index])

    if messagelength % keylength:                      # Add buffer letters for null places
        mk = messagelength % keylength
        kl = keylength - (messagelength%keylength)
        for i in range(kl):
            cipher[key[mk]].append(buffer_letters[i%len(buffer_letters)])
            mk += 1

    cipher_text = ""                                   # Rearrange the columns according to 'new_key'
    for i in new_key:
        x = ''.join(cipher[i])
        cipher_text = cipher_text+' '+x

    print(cipher_text.lstrip())                        #The extra kl variable lets the decrypt function
    decrypt(cipher_text.replace(" ",""), key, kl)      #know how many buffer letters were added


def decrypt(cipher_text, key, kl):
    cipher_len = len(cipher_text)
    keylength = len(key)
    cols = cipher_len // keylength
    old_key = OrderedDict()
    decipher = {}

    for i in key:                                      #Finding the order in which key should be arranged for encryption
        old_key[ord(i)] = i
    new_key = ''.join(OrderedDict(sorted(old_key.items())).values())

    for i in new_key:
        decipher[i] = []                               #Initialize 'decipher' dictionary by new_key


    chunks = [cipher_text[k + x * cols] for k in range(cols) for x in range(keylength)]  #Extracting chunks in message
    chunks = [chunks[i:i + keylength] for i in range(0, len(chunks), keylength)]         #according to number of columns

    for x in range(keylength):                         #Fill decipher dictionary with extracted chunks
        for i in range(cols):
            decipher[new_key[x]].append(chunks[i][x])
    plaintext = ""
    for x in range(cols):                              #map dict to key (original order of columns)
        for i in key:
            plaintext=plaintext+(decipher[i][x])

    plaintext = plaintext[:cipher_len-kl]              #Remove buffer letters
    print(plaintext)


message = 'wearediscoveredfleeatonce'
key = "players"                                        #Key and message is not protected here
encrypt(message, key)