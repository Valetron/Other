import itertools
import os
import pyautogui
import pyperclip
import time
import random

TEXT_BOX_COORDS = (205, 335)
PASTE_COORDS_1 = (234, 422)
PASTE_COORDS_2 = (281, 417)
BUTTON_COORDS = ((360, 517), (360, 414))
COLOR = (204, 204, 204)

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

def main():
	COUNT = 0
	start = int(input("the last key >> ")) # 16118
	
	CHARS = "BCDFGHJKMPQRTVWXY"
	NUMS = "2346789"
	key = ""
	for i in range(25):
		char = CHARS[random.randint(0, len(CHARS) - 1)]
		num = NUMS[random.randint(0, len(NUMS) - 1)]
		symbols = (char, num)
		key += random.choice(symbols)
	pyautogui.click(TEXT_BOX_COORDS[0], TEXT_BOX_COORDS[1], clicks = 3, duration = 0.5)
	pyautogui.click(button = "right")
	pyautogui.click(PASTE_COORDS_1[0], PASTE_COORDS_1[1], duration = 0.5)
	pyautogui.click(button="left")

	# for i in itertools.combinations_with_replacement("BCDFGHJKMPQRTVWXY2346789", 25):
	while True:
		COUNT+=1
		print(COUNT)
		if (start > COUNT):
			pass
		else:	
			# current_key = str(''.join(i))
			current_key = gen_key()
			if (len(set(current_key)) > 4):
				pyperclip.copy(current_key)
				pyautogui.click(TEXT_BOX_COORDS[0], TEXT_BOX_COORDS[1], clicks = 3, duration = 0.1)
				pyautogui.click(button = "right")
				pyautogui.click(PASTE_COORDS_2[0], PASTE_COORDS_2[1], duration = 0.1)
				pyautogui.click(button="left")
				time.sleep(1.5)
				if (pyautogui.pixelMatchesColor(BUTTON_COORDS[0][0], BUTTON_COORDS[0][1], COLOR)):
					# input(">>")
					continue
				elif (pyautogui.pixelMatchesColor(BUTTON_COORDS[1][0], BUTTON_COORDS[1][1], COLOR)):
					# input(">>")
					continue
				else:
					print("ERROR")
					print(pyautogui.position())
					print(pyautogui.pixel(BUTTON_COORDS[0][0], BUTTON_COORDS[0][1]))
					print(pyautogui.pixel(BUTTON_COORDS[1][0], BUTTON_COORDS[1][1]))
					input(">>")
			else:
				pass

def screen():
	while True:
		print(pyautogui.position())
		print(pyautogui.pixel(pyautogui.position()[0], pyautogui.position()[1]))
		time.sleep(1)
		os.system("clear")

# screen()
main()