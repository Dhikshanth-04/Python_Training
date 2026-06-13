def sumPair(arr, k):
    res = sorted(arr)
    i = 0
    j = len(arr)-1
    while(i<j):
        sum = res[i]+res[j]
        if(sum==k):
            print(res[i],res[j])
            i+=1
            j-=1
        elif(sum>k):
            j-=1
        else:
            i+=1

n = int(input("Enter array size : "))
arr = []
for i in range(0,n,1):
    arr.append(int(input("Enter array elements : ")))
k = int(input("Enter target number : "))
sumPair(arr, k)