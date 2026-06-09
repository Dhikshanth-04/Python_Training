def binarySearch(arr, k):
    left = 0
    right = len(arr)-1
    while(left<right):
        mid = (left+right)//2
        if(arr[mid] == target):
            return mid
        elif(arr[mid]>target):
            mid = left+1
        else:
            mid = right-1


    return 1

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
target = int(input("Enter target element : "))
res = binarySearch(arr, target)
print("The position : ",res)
