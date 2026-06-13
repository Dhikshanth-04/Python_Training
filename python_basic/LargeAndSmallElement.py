def findLargeSmallElement(arr):
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i>max:
            max = i
        elif i<min:
            min = i
    print("Max: ",max, "min: ",min)

n = int(input("Enter array size : "))
arr = []
for i in range(0,n,1):
    arr.append(int(input("Enter array elements : ")))
findLargeSmallElement(arr)