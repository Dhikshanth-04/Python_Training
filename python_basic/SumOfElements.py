def sumAvgOfElements(arr):
    sum = 0
    for i in arr:
        sum+=i
    return sum

n = int(input("Enter array size : "))
arr = []
for i in range(0,n,1):
    arr.append(int(input("Enter array elements : ")))
res = sumAvgOfElements(arr)
print("Sum :",res,"Average :",res/n)