def countOddEven(arr):
    even = 0
    odd = 0
    for i in arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
    print("odd: ",odd,"Even: ",even)

arr = []
size = int(input("Enter array size : "))
for i in range(size):
    arr.append(int(input("Enter array element : ")))
countOddEven(arr)
