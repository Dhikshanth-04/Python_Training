def secondLargest(arr):
    max = float('-inf')
    smax = float('-inf')
    for i in arr:
        if i>max:
            smax = max
            max = i
        elif i!=max and i>smax:
            smax = i
    return smax

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
res = secondLargest(arr)
if res == float('-inf'):
    print("No second largest element")
else:
    print(res)