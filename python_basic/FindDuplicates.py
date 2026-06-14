def findDuplicates(arr):
    freq = {}
    for i in arr:
        freq[i] = freq.get(i,0)+1
    for i in freq:
        if(freq[i]!=1):
            print(i)
    print(freq)

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
findDuplicates(arr)