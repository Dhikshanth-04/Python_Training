def ArrayRotation(arr,k):
    for i in range(k, len(arr), 1):
        print(arr[i])
    for i in range(0, k, 1):
        print(arr[i])

n = int(input("Enter array size : "))
arr = []
for i in range(0,n,1):
    arr.append(int(input("Enter array elements : ")))
k = int(input("Enter rotation number : "))
ArrayRotation(arr,k)