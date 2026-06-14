def missingNumber(arr):
    obsSum = sum(arr)
    n = len(arr)+1
    actSum = (n * (n+1))//2
    return actSum - obsSum

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
print(missingNumber(arr))