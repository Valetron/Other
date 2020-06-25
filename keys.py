import itertools
import random

def get_key():
    key1 = ""
    for i in itertools.combinations_with_replacement("2346789bcdfghjkmpqrtvwxy", 25):
        key1 = str(''.join(i))
        if (len(set(key1)) == 16):
            key2 = ""
            for i in range(25):
                if (i % 5 == 0 and i != 0):
                    key2 += '-' + key1[i]
                else:
                    key2 += key1[i]
            with open("TESTED_KEYS.txt", 'a') as file:
                file.write(key2 + "\n")
            # input(">> ")
        elif (len(set(key1)) > 16):
            break
        print(key1)
    print("END.")

def rand_key():
    SYMBOLS = "2346789bcdfghjkmpqrtvwxy"
    key = ""
    for i in range(25):
        if (i % 5 == 0 and i != 0):
            key += '-' + SYMBOLS[random.randrange(0, 24)]
        else:
            key += SYMBOLS[random.randrange(0, 24)]
    if (len(set(key)) < 14):
        return False
    else:
        return key

print(bool(rand_key()))
# get_key()