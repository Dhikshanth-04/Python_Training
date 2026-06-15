def slidingWindow(arr, k):
    winSum = sum(arr[:k])
    maxSum = winSum
    n = len(arr)
    for i in range(k,n):
        winSum+=arr[i]
        winSum-=arr[i-k]
        maxSum = max(winSum, maxSum)
    return maxSum

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
k = int(input("Enter window size : "))
res = slidingWindow(arr,k)
print(res)