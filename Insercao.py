# Bubble Sort ;-;
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Selection Sort 
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Insertion Sort
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


arr = [64, 25, 12, 22, 11, 9]
print("Array original:", arr)

bubbleSort(arr)
print("Bubble Sort:", arr)

arr = [64, 25, 12, 22, 11, 9]
selectionSort(arr)
print("Selection Sort:", arr)

arr = [64, 25, 12, 22, 11, 9]
insertionSort(arr)
print("Insertion Sort:", arr)