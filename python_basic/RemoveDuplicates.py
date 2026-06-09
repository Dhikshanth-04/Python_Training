def removeDuplicate(arr):
    res = set()
    for i in arr:
        res.add(i)
    return res 


arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
res = removeDuplicate(arr)
print("After removing duplicates : ", res)