def moveZerosToEnd(arr):
    res = []
    for i in arr:
        if i!=0:
            res.append(i)
    
    for i in arr:
        if i==0:
            res.append(i)
    return res

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
print(moveZerosToEnd(arr))