def subarray(arr):
    n = len(arr)

    for i in range(n):
        res = []
        for j in range(i, n):
            print(arr[i:j+1])

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
subarray(arr)