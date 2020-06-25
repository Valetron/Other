import itertools
import os
import requests
import bs4
import random

def get_key():
    key1 = ""
    for i in itertools.product("2346789bcdfghjkmpqrtvwxy", repeat = 25):
        if (len(set(str(''.join(i)))) == 16):
            key2 = str(''.join(i))
    for i in range(25):
        if (i % 5 == 0):
            key1 += '-' + key2[i]
        else:
            key1 += key2[i]
    return key1

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

def test():
    # last_iteration = int(input("Last iteration: "))
    # iterations = -1
    # symbols = "1234567890qwertyuiopasdfghjklzxcvbnm"
    session = requests.Session()
    session_id = 999999999999
    while (session_id != -1):
        key = rand_key()
        if (key):
            url = "https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows7&query=&action=GetSkuInformationByKey&key={}&sessionId=7afbaaa3-bb9a-4cdb-8bb3-{}&sdVersion=2".format(key, session_id)
            page = session.post(url)
            var = bs4.BeautifulSoup(page.text, features = "lxml")
            k = 0
            for j in var.recursiveChildGenerator():
                if (j.name):
                # print(j.name)
                    k += 1
            if (k > 16):
                print("DONE")
                print(key)
                input(">>")
            # print(k)
            session_id += -1
        else:
            pass

test()
# print(len(set("9chdfw4dhw74trv28gtr2yfbw")))