def firstUnique(str1):
    freq= {}
    for i in str1:
        freq[i] = freq.get(i,0)+1
    for i in str1:
        if freq[i] == 1:
            return i
    return -1
        

str1 = input("Enter string : ")
res = firstUnique(str1)
print(res)

