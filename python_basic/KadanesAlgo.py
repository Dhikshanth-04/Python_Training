def kadanesAlog(arr):
    currSum = arr[0]
    maxSum = arr[0]
    for i in range(1, len(arr)):
        currSum = max(arr[i], currSum+arr[i])
        maxSum = max(maxSum, currSum)
    return maxSum

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
res = kadanesAlog(arr)
print(res)