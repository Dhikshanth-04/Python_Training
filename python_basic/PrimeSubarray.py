def checkPrime(n):
    if n<=1:
        return False
    elif n==2 or n==3:
        return True
    elif n%2==0 or n%3==0:
        return False
    i = 5
    while(i*i<=n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

def allSubarray(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            res = arr[i:j+1]

            if checkPrime(sum(res)):
                print(res)

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
allSubarray(arr)