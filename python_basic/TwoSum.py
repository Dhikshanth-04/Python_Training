list1 = []
n = int(input("Enter the array size : "))
for i in range(n):
    list1.append(int(input("Enter element : ")))
k = int(input("Enter the target element : "))
i = 0
j = len(list1)-1
while(i<j):
    if(list1[i]+list1[j]==k):
        print(list1[i],list1[j])
        i+=1
        j-=1
    elif (list1[i]+list1[j]<k):
        i+=1
    else:
        j-=1
