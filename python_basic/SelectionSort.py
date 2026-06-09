def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if(arr[j]<arr[min]):
                min = j
        arr[i], arr[min] = arr[min], arr[i]

    return arr


arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
print("Before sorting : ", arr)
res = selectionSort(arr)
print("After sorting : ", res)