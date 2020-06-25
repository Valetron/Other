def bubble_sort(array):
	compare = 0
	transpos = 0
	for i in range(len(array) - 1):
		for j in range(len(array) - 1):
			compare += 1
			if (array[j] > array[j + 1]):
				array[j], array[j + 1] = array[j + 1], array[j]
				transpos += 1
	return (compare, transpos)

def bubble_super_sort(array):
	compare = 0
	transpos = 0
	for i in range(len(array)):
		swaped = False
		for j in range(len(array) - i - 1):
			compare += 1
			if (array[j] > array[j + 1]):
				array[j], array[j + 1] = array[j + 1], array[j]
				transpos += 1
				swaped = True
		if (not swaped):
			break
	return (compare, transpos)

def selection_sort(array):
	compare = 0
	transpos = 0
	for i in range(len(array)):
		smallest = i
		for j in range(i + 1, len(array)):
			compare += 1
			if (array[smallest] > array[j]):
				smallest = j
		if (smallest != i):
			array[i], array[smallest] = array[smallest], array[i]
			transpos += 1
	return (compare, transpos)

def insert_sort(array):
	compare = 0
	transpos = 0
	for i in range(len(array)):
		tmp = array[i]
		key = i
		while (key > 0 and array[key - 1] > tmp):
			key -= 1
			array[key + 1] = array[key]
			compare += 1
			transpos += 1
		array[key] = tmp
	return (compare, transpos)

def shaker_sort(array):
	compare = 0
	transpos = 0
	for i in range(len(array) // 2):
		j = 0
		while (j < len(array) - 1):
			compare += 1
			if (array[j] > array[j + 1]):
				array[j], array[j + 1] = array[j + 1], array[j]
				transpos += 1
			j += 1
		j = len(array) - 2
		while (j > 0):
			compare += 1
			if (array[j] > array[j + 1]):
				array[j], array[j + 1] = array[j + 1], array[j]
				transpos += 1
			j -= 1
	return (compare, transpos)

def shell_sort(array):
	compare = 0
	transpos = 0
	step = int(len(array) // 2)
	count = 0
	while (step > 0):
		for i in range(len(array)):
			tmp = array[i]
			key = i
			while (key > step - 1 and array[key - step] > tmp):
				key -= step
				array[key + step] = array[key]
				compare += 1
				transpos += 1
			array[key] = tmp
		step = int(step / 2)
	return (compare, transpos)