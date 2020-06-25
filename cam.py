import itertools
import random
import requests
from bs4 import BeautifulSoup
import os
import time

# r = requests.get('https://www.microsoft.com/ru-ru/software-download/windows7')
# r = requests.get('https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows7&query=&action=GetSkuInformationByKey&key=9chdf-w4dhw-74trv-28gtr-2yfbw&sessionId=727dbc3a-7634-4e5b-89e4-a3a97d1a1a09&sdVersion=2')
# r = requests.get('https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows7&query=&action=GetSkuInformationByKey&key=9chdf-w4dhw-74trv-28gtr-2yf3w&sessionId=727dbc3a-7634-4e5b-89e4-a3a97d1a1a09&sdVersion=2')
# print(r.status_code)
# for i in r.headers: 
    # print(i)

def gen_key():
	CHARS = "BCDFGHJKMPQRTVWXY"
	NUMS = "2346789"
	key = ""
	for i in range(25):
		char = CHARS[random.randint(0, len(CHARS) - 1)]
		num = NUMS[random.randint(0, len(NUMS) - 1)]
		symbols = (char, num)
		key += random.choice(symbols)
	return key

def not_main():
    with open("TESTED_KEYS.txt", 'a') as file:
        count = 0
        last_key = int(input("Последний: "))
        FRST_URL = "https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows7&query=&action=GetSkuInformationByKey&key="
        LST_URL = "&sessionId=727dbc3a-7634-4e5b-89e4-a3a97d1a1a09&sdVersion=2"
        for i in itertools.combinations_with_replacement("BCDFGHJKMPQRTVWXY2346789", 25):
            count += 1 # 11000
            print(count)
            if last_key <= count:
                key = str(''.join(i))
                url = FRST_URL + key + LST_URL
                r = requests.get(url)
                if ( r.headers['Content-Length'] == '669'):
                    time.sleep(1)
                    continue
                elif ( r.headers['Content-Length'] == '984' ):
                    # print(key)
                    file.write(key + '\n')
                else:
                    print("ERROR ", key, r.status_code)
                    input()
            else:
                pass

def main():
    count = 0
    last_key = int(input("Последний: "))
    FRST_URL = "https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows7&query=&action=GetSkuInformationByKey&key="
    LST_URL = "&sessionId=727dbc3a-7634-4e5b-89e4-a3a97d1a1a09&sdVersion=2"
    while True:
        count += 1 # 8814
        print(count)
        if last_key <= count:
            key = gen_key()
            url = FRST_URL + key + LST_URL
            r = requests.get(url)
            if ( r.headers['Content-Length'] == '669'):
                time.sleep(1)
                continue
            elif ( r.headers['Content-Length'] == '984' ):
                # print(key)
                file = open("TESTED_KEYS.txt", 'a')
                file.write(key + '\n')
                file.close()
            else:
                print("ERROR ", key, r.status_code)
                input()
        else:
            pass

# r1 = requests.get('https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526&host=www.microsoft.com&segments=software-download%2cwindows7&query=&action=GetSkuInformationByKey&key=9chdf-w4dhw-74trv-28gtr-2yfbw&sessionId=727dbc3a-7634-4e5b-89e4-a3a97d1a1a09&sdVersion=2')
# r2 = requests.get('https://www.microsoft.com/ru-ru/software-download/windows7')
# r3 = requests.get('https://www.microsoft.com/ru-ru/api/controls/contentinclude/html?pageId=cd06bda8-ff9c-4a6e-912a-b92a21f42526')
# print(r2.headers)
# s = BeautifulSoup(r2.content, 'html.parser')
# print(s.select('.CSPvNext loaded'))
# print(s.find("input", id="session-id"))
# tags = s.find_all('script')
# for i in tags:
#     print(i)
#     input()
#     os.system('clear')

# for child in s.recursiveChildGenerator(): 
#     if child.name == 'script':
#         print('WORK')

# print(s.select("#session-id"))

# print(r2.text)
# print(type(r.headers['Content-Length']))
# заголовок content-lenght: 669 -> ошибка, 984 -> робит
main()