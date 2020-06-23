# print("\n")
# print("1.1. Вывод Hello World\n")
# print("Hello World")
#===============================================================
# print("\n")
# print("1.2. Ввод числа с клавиатуры")
# print("1.3. Вывод числа на экран\n")
# UserInput = int(input("Введите число: "))
# print("Вы ввели: ", UserInput)
#===============================================================
# print("\n")
# print("1.4. Сложение 2-х чисел\n")
# UserInput1 = int(input("Введите первое число: "))
# UserInput2 = int(input("Введите второе число: "))
# sum = UserInput1 + UserInput2
# print("Сумма = ", sum)
#===============================================================
# print("\n")
# print("1.5. Умножение 2-х чисел\n")
# UserInput1 = int(input("Введите первое число: "))
# UserInput2 = int(input("Введите второе число: "))
# compos = UserInput1 * UserInput2
# print("Произведение = ", compos)
#===============================================================
# print("\n")
# print("1.6. Вывод остатка деления двух чисел\n")
# UserInput1 = int(input("Введите делимое: "))
# UserInput2 = int(input("Введите делитель: "))
# ost = UserInput1 % UserInput2
# print("Остаток от деления = ", ost)
#===============================================================
# print("\n")
# print("1.7. Перевод секунд в часы\n")
# UserInput = int(input("Введите секунды: "))
# hours = UserInput / 3600
# print("Часов: ", hours)
#===============================================================
# print("\n")
# print("1.8. Перевод фунтов в граммы\n")
# UserInput = int(input("Введите фунты: "))
# grams = UserInput * 453, 592
# print("Граммов: ", grams)
#===============================================================
# print("\n")
# print("1.9. Перевод секунд в часы-минуты-секунды\n")
# UserInput = int(input("Введите количество секунд: "))
# hours = int(UserInput / 3600)
# minutes = int((UserInput - hours * 3600) / 60)
# seconds = int((UserInput - (hours * 3600 + minutes * 60)))
# print("Часов - ", hours, "\nМинут - ", minutes, "\nСекунд - ", seconds)
#===============================================================
# print("\n")
# print("1.10. Замена значений в A и B без заведения третьей переменной\n")
# UserInput1 = int(input("Введите число A: "))
# UserInput2 = int(input("Введите число B: "))
# UserInput2 = UserInput2 + UserInput1
# UserInput1 = UserInput2 - UserInput1
# UserInput2 = UserInput2 - UserInput1
# print("Число A - ", UserInput1, "\nЧисло B - ", UserInput2)
#===============================================================
# print("\n")
# print("2.1. Вывести на экран большее из двух чисел\n")
# UserInput1 = int(input("Введите число A: "))
# UserInput2 = int(input("Введите число B: "))
# if (UserInput1 > UserInput2):
#     print("Число A - ", UserInput1, "больше\n")
# elif (UserInput1 < UserInput2):
#     print("Число B - ", UserInput2, "больше\n")
# else:
#     print("Числа равны\n")
#===============================================================
# print("\n")
# print("2.2. Определение високосного года\n")
# UserInput = int(input("Введите год: "))
# if ((UserInput % 4 != 0) or ((UserInput % 100 == 0) and (UserInput % 400 != 0))):
#     print(UserInput , "- год не високосный\n")
# else:
#     print(UserInput, "- год високосный\n")
#===============================================================
# print("\n")
# print("2.3. Определение возраста\n")
# UserInput = int(input("Введите свой год рождения: "))
# year  = int(input("Введите настоящий год: "))
# Age = year - UserInput
# Age1 = Age % 10
# Age2 = Age % 100
# if ((Age1 == 1) and (Age2 != 11)):
#     print("Вам -", Age, "год\n")
# elif (Age1 >= 2 and Age1 <= 4 and (Age2 < 10 or Age2 >= 20)):
#     print("Вам -", Age, "года\n")
# else:
#     print("Вам -", Age, "лет\n")
#===============================================================
# print("\n")
# print("2.4. Кирпич и стена\n")
# Wall_1 = int(input("Введите длину отверстия: "))
# Wall_2 = int(input("Введите ширину отверстия: "))
# Brick_1 = int(input("Введите длину кирпича: "))
# Brick_2 = int(input("Введите ширину кирпича: "))
# Brick_3 = int(input("Введите высоту кирпича: "))
# if ((Wall_1 >= Brick_1) and (Wall_2 >= Brick_2)):
#     print("Кирпич пройдет")
# elif ((Wall_1 >= Brick_2) and (Wall_2 >= Brick_3)):
#     print("Кирпич пройдет")
# elif ((Wall_1 >= Brick_1) and (Wall_2 >= Brick_3)):
#     print("Кирпич пройдет")
# else:
#     print("Кирпич не пройдет")
#===============================================================
# print("\n")
# print("2.5. Калькулятор\n")
# while(True):
#     print("\t\tМЕНЮ\n\t1 - сложить\n\t2 - вычесть\n\t3 - умножить\n\t4 - разделить\n\t5 - выйти\n")
#     menu = int(input(">> "))
#     if (menu == 1):
#         Num1 = int(input("Введите первое слагаемое: "))
#         Num2 = int(input("Введите второе слагаемое: "))
#         Result = int(Num1 + Num2)
#         print("Ответ", Result)
#     elif (menu == 2):
#         Num1 = int(input("Введите уменьшаемое: "))
#         Num2 = int(input("Введите вычетаемое: "))
#         Result = int(Num1 - Num2)
#         print("Ответ", Result)
#     elif (menu == 3):
#         Num1 = int(input("Введите первый множитель: "))
#         Num2 = int(input("Введите второй множитель: "))
#         Result = int(Num1 * Num2)
#         print("Ответ", Result)
#     elif (menu == 4):
#         Num1 = int(input("Введите делимое: "))
#         Num2 = int(input("Введите делитель: "))
#         Result = int(Num1 / Num2)
#         print("Ответ", Result)
#     else:
#         break
#===============================================================
# print("\n")
# print("3.1. Вывод на экран чисел с 1 по N\n")
# UserInput = int(input("Введите число N: "))
# Num = 0
# while (Num < UserInput):
#     Num = Num + 1
#     print(Num)
#===============================================================
# print("\n")
# print("3.2. Вывод на экран четных чисел до N\n")
# UserInput = int(input("Введите число N: "))
# Num = 0
# while (Num < UserInput):
#     Num = Num + 1
#     if (Num % 2 == 0):
#         print(Num)
#     else:
#         continue
#===============================================================
# print("\n")
# print("3.3. Сложение N чисел\n")
# UserInput = int(input("Введите число: "))
# Num = 0
# N = 0
# while (N <= UserInput):
#     Num = Num + N
#     N = N + 1
#     print(Num)
#===============================================================
# print("\n")
# print("3.4. Вычисление факториала\n")
# UserInput = int(input("Введите число: "))
# Factorial = 1
# for i in range(1, UserInput + 1):
#     Factorial *= i
#     i += i
# print(UserInput, "!=", Factorial)
#===============================================================
# print("\n") # ошибка
# print("3.4. Вычисление факториала\n")
# def factorial(num):
# 	if (num <= 1):
# 		return 1
# 	else:
# 		return num * factorial(num - 1)
# UserInput = int(input("Введите число: "))
# print(factorial(UserInput))
#===============================================================
# print("\n")
# print("3.5. Лапы (Зайцы и Кролики)\n")
# i = 0
# rabits = 0
# ducks = 0
# foots = int(input("Введите количество ног: "))
# while i <= foots:
#     rabits = int((foots - i) / 4)
#     ducks = int((foots - (rabits * 4)) / 2)
#     print("Кроликов - ", rabits," ", "Уток - ", ducks)
#     i = i + 4
#===============================================================
# print("\n")
# print("4.1. Заполнение массива числами")
# array = [int(input("Элемент: ")) for i in range(int(input("Размер массива: ")))]
# print(array)
#===============================================================
# print("\n")
# print("4.2. Подсчет частоты встречаемости числа в массиве")
# import random
# array = [random.randint(0, 9) for i in range(int(input("Размер массива: ")))]
# UserInput = int(input("Число для подсчета: "))
# rate = 0
# for i in range(len(array)):
# 	if UserInput == array[i]:
# 		rate += 1
# print("Число {} встретилось {} раз(а)".format(UserInput, rate))
#===============================================================
# print("\n")
# print("4.3. Перестановка в массиве 0 и 1")
# import random
# array = [random.randint(0, 1) for i in range(int(input("Размер массива: ")))]
# print(array)
# for i in range(len(array) - 1):
# 	for j in range(i, len(array)):
# 		if (array[i] == 1) and (array[j] == 0):
# 			tmp = array[i] 
# 			array[i] = array[j]
# 			array[j] = tmp
# print(array)
#===============================================================
# print("\n") # чем больше массив, тем чаще ошибка
# print("4.4. Удаление 0 из массива")
# import random
# array = [random.randint(0, 9) for i in range(int(input("Размер массива: ")))]
# print(array)
# i = 0
# # while (0 in array):
# while ((0 in array) or (i == len(array))):
# 	i += 1
# 	if (array[i] == 0):
# 		array0 = array[:i]
# 		array1 = array[i + 1:]
# 		array = array0 + array1
# print(array)
#===============================================================
# print("\n")
# print("4.5. Сложение всех элементов массива")
# import random
# array = [random.randint(0, 9) for i in range(int(input("Размер массива: ")))]
# print(array)
# sum = 0
# for i in range(len(array)):
# 	sum += array[i]
# print(sum)
#===============================================================
# print("\n")
# print("4.6. Последовательное сложение элементов массива")
# array = [[] for i in range(int(input("Размер массива: ")))]
# array[0] = int(input("Первый элемент: "))
# array[1] = 0 + array[0]
# for i in range(2, len(array)):
# 	array[i] = array[i - 1] + array[i - 2]
# print(array)
#===============================================================
# print("\n")
# print("4.7. Запись в массив C элементов из массива A, которые есть в массиве B")
# import random 
# arrayA = [random.randint(0, 99) for i in range(int(input("Размер массива A: ")))]
# arrayB = [random.randint(0, 99) for i in range(int(input("Размер массива B: ")))]
# arrayC = []
# for i in range(len(arrayA)):
# 	if ((arrayA[i] in arrayB) and (arrayA[i] not in arrayC)):
# 		arrayC.append(arrayA[i])
# print(arrayC)
#===============================================================
# print("\n")
# print("4.8. Заполнение двумерной матрицы с клавиатуры")
# rows = int(input("Строк: "))
# colums = int(input("Столбов: "))
# Matrix = [[[] for j in range(colums)] for i in range(rows)]
# print("Матрица")
# for i in range(rows):
#     for j in range(colums):
#         Matrix[i][j] = int(input(">> "))
# for i in range(rows):
#     for j in range(colums):
#         print(Matrix[i][j], end = " ")
#     print("\n")
#===============================================================
# print("\n")
# print("4.9. Зеркальное отображение квадратной матрицы")
# import random
# rows = int(input("Размер матрицы: "))
# colums = rows
# Matrix = [[[] for j in range(colums)] for i in range(rows)]
# diag = random.randint(0, 9)
# for i in range(rows):
# 	for j in range(colums):
# 		if (i == j) and (j == i):
# 			Matrix[i][j] = diag
# 			Matrix[j][i] = diag
# 		else:
# 			Matrix[i][j] = random.randint(0, 9)
# 			Matrix[j][i] = Matrix[i][j]
# for i in range(rows):
#     for j in range(colums):
#         print(Matrix[i][j], end = " ")
#     print("\n")
#===============================================================
# print("\n")
# print("5.1. Подсчет символа 'с' в строке\n")
# UserInput = input("Введите строку: ")
# print(UserInput.count('c'))
#===============================================================
# print("\n")
# print("5.2. Замена символа 'A' на символ 'B'\n")
# UserInput = input("Введите строку: ")
# print(UserInput.replace('A', 'B'))
#===============================================================
# print("\n")
# print("5.3. Зеркально отобразить строку\n")
# UserInput = input("Введите строку: ")
# print(UserInput[::-1])
#===============================================================
# print("\n")
# print("5.4. Удалить все пробелы\n")
# UserInput = input("Введите строку: ")
# print(UserInput.replace(' ', ''))
# STR = UserInput.split()
# print(''.join(STR))
#===============================================================
# print("\n")
# print("5.5. Удалить лишние пробелы\n")
# UserInput = input("Введите строку: ")
# print(' '.join(UserInput.split()))
#===============================================================
# print("\n")
# print("5.6. Разбить строку на слова\n")
# UserInput = input("Введите строку: ")
# Words = UserInput.split()
# for i in range(len(Words)):
#     print(Words[i])
#===============================================================
# print("\n") #сомнения насчет правильности, лексикографически???
# print("5.7. Сравнить две строки\n")
# UserInput1 = input("Введите первую строку: ")
# UserInput2 = input("Введите вторую строку: ")
# if (UserInput1 > UserInput2):
#     print("Строка 1 больше\n")
# elif (UserInput1 < UserInput2):
#     print("Строка 2 больше\n")
# else:
#     print("Строки равны\n")
#===============================================================
# print("\n")
# print("5.8. Запись в строку C слова из строки A, которые есть в строке B\n")
# string1 = [input(">> ") for i in range(int(input("Кол-во слов в 1 строке: ")))]
# string2 = [input(">> ") for i in range(int(input("Кол-во слов во 2 строке: ")))]
# string3 = []
# for i in range(0, len(string1)):
# 	for j in range(i, len(string1)):
# 	    if (string2[j] == string1[i]):
# 	        string3.append(string1[i])
# print(string3)
#===============================================================
# print("\n") #доделать с исключениями
# print("5.9. Преобразовать строку в целое число\n")
# UserInput = input("Введите строку: ")
# print(type(int(UserInput)), "\n", (int(UserInput)))
#===============================================================
# print("\n") #доделать с исключениями
# print("5.10. Преобразовать строку в число с плавающей точкой\n")
# UserInput = input("Введите строку: ")
# print(type(float(UserInput)), "\n", (float(UserInput)))
#===============================================================
# print("\n") #доделать
# print("5.11. Найти в строке str1 все вхождения подстроки str2\n")
# UserInput1 = input("Введите строку: ")
# UserInput2 = input("Введите подстроку: ")
# count = 0
# str1 = UserInput1.split()
# for i in range(0, len(str1)):
#     if (UserInput2 == str1[i]):
#         count += 1
# print(count)
#===============================================================
# print("\n")
# print("5.12. Заполнить динамический двумерный массив строками\n")
# string = [input(">> ") for i in range(int(input("Размер массива: ")))]
# print("\n")
# print(string)
#===============================================================
# print("\n")
# print("5.13. Определить больше ли строка A строки B \n")
# UserInput1 = input("Введиет первую строку: ")
# UserInput2 = input("Введиет вторую строку: ")
# if (UserInput1 > UserInput2):
#     print("Первая строка больше\n")
# elif (UserInput1 < UserInput2):
#     print("Вторая строка больше\n")
#===============================================================
# print("\n")
# print("5.14. Отсортировать двумерный массив строк\n")
# array = [input(">> ") for i in range(int(input("Размер массива: ")))]
# t = int(len(array)/2)
# while t > 0:
# 	for i in range(len(array) - t):
# 		j = i
# 		while j >= 0 and array[j] > array[j + t]:
# 			array[j], array[j + t] = array[j + t], array[j]
# 			j -= 1
# 	t = int(t/2)
# print(array)
#===============================================================
# from random import randint
# print("\n")
# print("6.1. Сортировка пузырьком\n")
# UserInput = int(input("Введите размер массива: "))
# a = []
# for i in range(UserInput):
#     a.append(randint(0, 10))
# print("Было: \n", a)
# for i in range(UserInput):
#     for j in range(UserInput - i - 1):
#         if (a[j] > a[j + 1]):
#             tmp = a[j + 1]
#             a[j + 1] = a[j]
#             a[j] = tmp
# print("\nСтало: \n", a)
#===============================================================
# from random import randint 
# print("\n")
# print("6.2. Сортировка вставкой\n")
# array = [randint(0, 9) for i in range(int(input("Размер массива: ")))]
# print("Было: \n", array)
# for i in range(len(array)):
# 	v = array[i]
# 	j = i
# 	while (array[j - 1] > v) and (j > 0):
# 		array[j] = array[j - 1]
# 		j = j - 1
# 	array[j] = v
# print("\nСтало: \n", array)
#===============================================================
# from random import randint 
# print("\n")
# print("6.3. Сортировка выбором\n")
# array = [randint(0, 9) for i in range(int(input("Размер массива: ")))]
# print("Было: \n", array)
# for i in range(len(array)):
# 	Min = i
# 	for j in range(i+1, len(array)):
# 		if array[j] < array[Min]:
# 			Min = j
# 	tmp = array[Min]
# 	array[Min] = array[i]
# 	array[i] = tmp
# print("\nСтало: \n", array)
#===============================================================
# print("\n")
# print("7.1. Запись числа в файл\n")
# with open("f.txt", 'w') as f:
# 	f.write(input("Введите число: "))
#===============================================================
# print("\n")
# print("7.2. Чтение числа из файла\n")
# with open("f.txt", 'r') as f:
# 	num = int(f.read())
# 	print("Число из файла -", num)
#===============================================================
# print("\n")
# print("7.3. Записать n чисел в файл")
# count = int(input("Количество чисел на запись: "))
# with open("f1.txt", 'w') as f1:
# 	for i in range(0, count):
# 		print("Введите число №{}".format(i + 1))
# 		f1.write(input(">> "))
# 		f1.write("\n")
#===============================================================
# print("\n")
# print("7.4. Считать n чисел из файла")
# with open("f1.txt", 'r') as f1:
# 	nums = f1.readlines()
# 	for i in range(0, len(nums)):
# 		num = int(nums[i])
# 		print("Число №{} - {}".format(i + 1, num))
#===============================================================
# print("\n")
# print("7.5. Запись в файл массив")
# arraySize = int(input("Размер массива: "))
# myArray = []
# with open("f2.txt", 'w') as f2:
# 	for i in range(0, arraySize):
# 		print("Введите число №{}".format(i + 1))
# 		myArray.append((input(">> ")))
# 		f2.write(myArray[i])
# 		f2.write("\n")
#===============================================================
# print("\n")
# print("7.6. Считать из файла массив")
# a = []
# with open("f2.txt", 'r') as f2:
# 	for i in f2:
# 		a.append(i)
# print(a)
#===============================================================
# print("\n")
# print("7.7. Записать матрицу в файл")
# rows = int(input("Строк: "))
# colums = int(input("Столбов: "))
# matrix = [ [ [] for j in range(colums)] for i in range(rows) ]
# with open("f3.txt", 'w') as f3:
# 	f3.write(str(rows))
# 	f3.write("\n")
# 	f3.write(str(colums))
# 	f3.write("\n")
# 	for i in range(rows):
# 		for j in range(colums):
# 			matrix[i][j] = (input(">> "))
# 			f3.write(matrix[i][j])
# 			f3.write("\n")
# print(matrix)
#===============================================================
# print("\n")
# print("7.8. Считать матрицу из файла")
# with open("f3.txt", 'r') as f3:
# 	rows = int(f3.readline())
# 	print(rows)
# 	colums = int(f3.readline())
# 	print(colums)
# 	matrix = [ [ [] for j in range(colums)] for i in range(rows) ]
# 	for i in range(0, rows):
# 		for j in range(0, colums):
# 			matrix[i][j] = int(f3.readline())
# 	print(matrix)
#===============================================================
# print("\n")
# print("8.1. Разбор слова на приставку, корень, окончание\n")
# def addPrefix():
# 	with open("pristavki.txt", 'a') as file:
# 		prefix = input("Записать приставку: ")
# 		file.write(prefix)
# 		file.write("\n")

# def addRoot():
# 	with open("korni.txt", 'a') as file:
# 		root = input("Записать корень: ")
# 		file.write(root)
# 		file.write("\n")

# def addSuffix():
# 	with open("okoncania.txt", 'a') as file:
# 		suffix = input("Записать окончание: ")
# 		file.write(suffix)
# 		file.write("\n")

# def getPrefix():
# 	with open("pristavki.txt", 'r') as file:
# 		prefixes = file.readline()
# 		for i in prefixes:
# 			return i

# def getRoot():
# 	with open("korni.txt", 'r') as file:
# 		roots = file.readline()
# 		for i in roots:
# 			return i

# def getSuffix():
# 	with open("okoncania.txt", 'r') as file:
# 		suffixes = file.readline()
# 		for i in suffixes:
# 			return i

# def wordFunc():
# 	word = input("Введите слово: ")
# 	prefix = getPrefix()
# 	root = getRoot()
# 	suffix = getSuffix()
# 	if (prefix + root + suffix) == word:
# 		print("Приставка - {}\nКорень - {}\nОкончание - {}\n".format(prefix, root, suffix))
# 	elif (root in word):
# 		print("Корень - " + root)
# 	else:
# 		print("Невозможно разобрать слово")

# def main():
# 	print("===MENU===\n1 - Записать приставку\n2 - Записать корень\n3 - Записать окончание\n4 - Разобрать слово\n5 - выйти")
# 	menuUnput = int(input(">> "))
# 	while ( menuUnput != 5):
# 		if menuUnput == 1:
# 			addPrefix()
# 		elif menuUnput == 2:
# 			addRoot()
# 		elif menuUnput == 3:
# 			addSuffix()
# 		elif menuUnput == 4:
# 			wordFunc()
# 		else:
# 			print("Неверная команда\n")

# main()
#===============================================================
# import random
# while True:
# 	a = str(random.randint(0, 99))
# 	yield a

# def find_two_smallest (L):
# smallest = min (L)
# min1 = L.index (smallest)
# L.remove (smallest) # удаляем первый минимальный элемент
# next_smallest = min (L)
# min2 = L.index (next_smallest)
# L.insert (min1, smallest) # возвращаем первый минимальный обратно
# if min1 <= min2:  # проверяем индекс второго минимального из-за смещения
# min2 += 1 # min2 = min2 + 1
# return (min1, min2) # возвращаем кортеж

# def find_two_smallest (L):
# if L[0] < L[1]:
# min1, min2 = 0, 1 # устанавливаем начальные значения
# else:
# min1, min2 = 1, 0
# for i in range (2, len (L)):
# if L[i] < L[min1]: # «первый вариант»
# min2 = min1
# min1 = i
# elif L[i] < L[min2]: # «второй вариант»
# min2 = i
# return (min1, min2)


# class Cat():
# 	name = ""
# 	color = ""
# 	weight = 0
# 	def __init__(self):
# 		print("У вас кошка \a")
# 	def meow(self):
# 		print("ГАВ!")

# myCat = Cat()
# myCat.name = "ТИГхъ"
# myCat.color = "Оранжевый"
# myCat.weight = 20
# myCat.meow()

# class Dog():
# 	name=""
# 	# Конструктор вызывается в момент создания объекта этого класса
# 	def __init__ (self, newName):
# 		self.name = newName
# 	# Можем в любой момент вызвать метод и изменить имя собаки
# 	def setName (self, newName):
# 		self.name = newName
# 	# Можем в любой момент вызвать метод и узнать имя собаки
# 	def getName (self):
# 		return self.name # возвращаем текущее имя объекта

# # Создаем собаку с начальным именем:
# myDog = Dog ("Spot")
# # Выводим имя собаки:
# print (myDog.getName())
# # Установим новое имя собаки:
# myDog.setName("Sharik")
# # Посмотрим изменения имени:
# print (myDog.getName())

# class Animal():
# 	name = ""
# 	def __init__(self):
# 		print("Родилось - " + self.name)
# 	def getName(self):
# 		return self.name
# 	def setName(self, newName):
# 		self.name = newName
# 	def eat(self):
# 		print("Ням")
# 	def makeNoise(self):
# 		print(self.name + " говорит: Опааа зигота")

# class Cat(Animal):
# 	name = ""
# 	def __init__(self, newName):
# 		self.name = newName
# 		print("Родился кот")
# 		Animal.__init__(self)
# 	def makeNoise(self):
# 		print(self.name + " говорит Мяу")

# nameAnimal = input("Имя: ")
# newAnimal = Animal(nameAnimal)
# newAnimal = Cat(nameAnimal)
# newAnimal.Cat.makeNoise()

# class String():
# 	string = None
# 	def __init__(self, nameStr):
# 		self.string = nameStr
# 	def getStr(self):
# 		return self.string
# 	def setStr(self, newStr):
# 		self.string = newStr

# inputStr = input("Ввод: ")
# myStr = String(inputStr)
# print(myStr.getStr())
# newInputStr = input("Новая строка: ")
# myStr.setStr(newInputStr)
# print(myStr.getStr())

# class Student():
# 	name = None
# 	age = None
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
# 	def changeName(self, newName):
# 		self.name = newName
# 	def changeAge(self, newAge):
# 		self.age = newAge
# 	def showData(self):
# 		print(self.name)
# 		print(self.age)

# def output(var):
# 	for i in var:
# 		print("Имя - {}\nВозраст - {}\n".format(i.name, i.age))

# def delStud(array, position):
# 	del array[position]

# def main():
# 	count = int(input("Кол-во людей: "))
# 	studs = []
# 	for i in range(count):
# 		name = input("Имя: ")
# 		age = int(input("Возраст: "))
# 		a = Student(name, age)
# 		studs.append(a)
# 		print("\n")
# 	output(studs)
# 	pos = int(input("Человек № "))
# 	newName = input("Новое имя: ")
# 	studs[pos - 1].changeName(newName)
# 	newAge = int(input("Новый возраст: "))
# 	studs[pos - 1].changeAge(newAge)
# 	studs[pos - 1].showData()
# 	pos = int(input("Удалить человека № "))
# 	delStud(studs, pos - 1)
# 	output(studs)

# main()

# import tkinter
# window = tkinter.Tk()
# # Создаем объект класса StringVar и присваиваем указатель на него data
# # (создаем строковую переменную, с которой умеет работать tkinter)
# data = tkinter.StringVar()
# # Метод set класса StringVar позволяет изменить содержимое переменной:
# data.set ('Данные в окне')
# # textvariable присваиваем ссылку на строковый объект из переменной data
# label = tkinter.Label (window, textvariable = data)
# label.pack()
# window.mainloop()

# import tkinter
# window = tkinter.Tk()
# frame = tkinter.Frame(window)
# frame.pack()
# var = tkinter.StringVar()
# # Обновление содержимого переменной происходит в режиме реального времени
# label = tkinter.Label(frame, textvariable=var)
# label.pack()
# # Пробуем набрать текст в появившемся поле для ввода
# entry = tkinter.Entry(frame, textvariable=var)
# entry.pack()
# window.mainloop()

# import tkinter
# # Контроллер: функция вызывается в момент нажатия на кнопку
# def click():
# # метод get() возвращает текущее значение counter
# # метод set() – устанавливает новое значение counter
# 	counter.set(counter.get() + 1)
# window = tkinter.Tk()
# # Модель: создаем объект класса IntVar
# counter = tkinter.IntVar()
# # Обнуляем созданный объект с помощью метода set()
# counter.set(0)
# frame = tkinter.Frame (window)
# frame.pack()
# # Создаем кнопку и указываем обработчик (функция click) при нажатии на нее
# button = tkinter.Button(frame, text='Click', command=click)
# button.pack()
# # Вид: в реальном времени обновляется содержимое виджета Label
# label = tkinter.Label(frame, textvariable=counter)
# label.pack()
# window.mainloop()

import tkinter
window = tkinter.Tk()
# Модель:
counter = tkinter.IntVar()
counter.set(0)
# Два контроллера:
def click_up():
	counter.set (counter.get() + 1)
def click_down():
	counter.set (counter.get() - 1)
# Вид:
frame = tkinter.Frame (window)
frame.pack()
button = tkinter.Button (frame, text='Up', command=click_up)
button.pack()
button = tkinter.Button (frame, text='Down', command=click_down)
button.pack()
label = tkinter.Label (frame, textvariable=counter)
label.pack()
window.mainloop()