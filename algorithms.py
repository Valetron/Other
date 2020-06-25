import random

test_array = [random.randint(-100, 101) for i in range(random.randint(10, 101))]


def bin_search(array, item):
    low = 0
    high = len(array) - 1
    while (low <= high):
        mid = (low + high)
        guess = array[mid]
        if (guess == item):
            return mid
        elif (guess > item):
            high = mid - 1
        else:
            low = mid + 1



def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def selection_sort(array): # O(n^2)
    for i in range(len(array)):
        smallest = i
        for j in range(i + 1, len(array)):
            if (array[smallest] > array[j]):
                smallest = j
        if (smallest != i):
            array[i], array[smallest] = array[smallest], array[i]
    return array

def quick_sort(array):
    if (len(array) < 2):
        return array
    else:
        pivot = array[0] 
        less = [i for i in array[1:] if i < pivot]
        greater = [ i for i in array [1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def shell_sort(array):
    step = len(array) // 2
    count = 0
    while(step > 0):
        for i in range(len(array)):
            tmp = array[i]
            hole = i
            while((hole > step - 1) and (array[hole - step] > tmp)):
                hole -= step
                array[hole + step] = array[hole]
                count += 1
            array[hole] = tmp
        step = int(step / 2)
    return array


# print(test_array)
# print(quick_sort(test_array))
class Sorts():
    def my_sort(self, var):
        self.greet = "Hello, " + var
        return self.greet


class Mathematical():
    def name(self):
        pass

    def sieve_eratosthenes(self, n):
        array = set(range(2, n + 1))
        i = 2
        while (i ** 2 <= n):
            for j in range(i ** 2, n + 1, i):
                if (j in array):
                    array.discard(j)
            i += 1
        return array

    def count_inversions(self, array):
        count = 0
        for i in range(len(array) - 1):
            for j in range(i + 1, len(array)):
                if (array[i] > array[j]):
                    count += 1
        return count

                

class Other():
    def hello():
        print("Hello, World!")

    def max_find(self, array):
        max_num = array[0]
        for i in range(len(array)):
            if (max_num < array[i]):
                max_num = array[i]
        return max_num

    def min_find(self, array):
        min_num = array[0]
        for i in range(len(array)):
            if (min_num > array[i]):
                min_num = array[i]
        return min_num

if __name__ == "__main__":
    pass