import itertools
import os
import requests
import bs4
import random

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
    session = requests.Session()
    session_id = 999999999999
    while (session_id != -1):
        key = rand_key()
        if (key):
            url = "https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=027783cf-1326-4710-b8d1-e501d5d90886&host=www.microsoft.com&segments=software-download%2coffice&query=&action=GetSkuInformationByKey&key={}&sessionId=526fb410-f06d-4e79-a7ae-{}&sdVersion=2".format(key, session_id)
            page = session.post(url)
            var = bs4.BeautifulSoup(page.text, features = "lxml")
            k = 0
            for j in var.recursiveChildGenerator():
                if (j.name):
                    k += 1
            if (k > 16):
                print("DONE")
                print(key)
                input(">>")
            print(session_id)
            session_id += -1
        else:
            pass

test()