def kthLargest(arr,k):
    res = sorted(set(arr), reverse=True)
    if k>len(arr) or k<=0:
        return -1
    return res[k-1]

n = int(input("Enter array size : "))
arr = []
for i in range(0,n,1):
    arr.append(int(input("Enter array elements : ")))
k = int(input("Enter k : "))
res = kthLargest(arr,k)
print(res)