import random
import time
import pyperclip
import pyautogui
import time

ERROR_COLOR = (76, 76, 76)

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
	while True:
		pyperclip.copy( gen_key() )
		pyautogui.click(x = 480, y = 380, clicks = 3, button = "left")  # активировать форму
		pyautogui.click(button = "right")                               # нажать правой кнопкой
		pyautogui.click(x = 600, y = 465, clicks = 1, button = "left")  # вставить из буффера
		pyautogui.click(x = 465, y = 430, clicks = 1, button = "left")  # нажать кнопку
		# проверить наличие окна ошибки
		pix = pyautogui.pixel(190, 240)
		time.sleep(2)
		if (pix[:] == ERROR_COLOR):
			pyautogui.click(x = 802, y = 676, clicks = 1, button = "left") # закрыть окно ошибки
		else:
			break

def main_2():
	with open("NEW_KEYS.txt", 'r') as keys:
		lines = keys.readlines()
		for i in range(391, len(lines)):
			lines[i] = lines[i].replace("\n", '')
			pyperclip.copy( lines[i] )
			pyautogui.click(x = 605, y = 345, clicks = 3, button = "left", duration = 0.25)  # активировать форму
			pyautogui.click(button = "right")                               # нажать правой кнопкой
			pyautogui.click(x = 665, y = 440, clicks = 1, button = "left", duration = 0.25)  # вставить из буффера
			pyautogui.click(x = 470, y = 435, clicks = 1, button = "left", duration = 0.25)  # нажать кнопку
			# проверить наличие окна ошибки
			pix = pyautogui.pixel(190, 240)
			time.sleep(3)
			if (pix[:] == ERROR_COLOR):
				pyautogui.click(x = 765, y = 755, clicks = 1, button = "left", duration = 0.25) # закрыть окно ошибки
				pyautogui.click(x = 750, y = 685, clicks = 1, button = "left", duration = 0.25)
				pyautogui.click(x = 800, y = 750, clicks = 1, button = "left", duration = 0.25)
				# pyautogui.click(x = 750, y = 720, clicks = 1, button = "left")

			else:
				print(i)
				break
		# print(len(lines))

main()
print(pyautogui.position())

# with open("keys.txt", 'r') as file1:
# 	data = file1.readlines()
# 	print(len(data))
# with open("NEW_KEYS.txt", 'w') as file2:
# 	data = list(set(data))
# 	for i in range(len(data)):
# 		file2.write(data[i])