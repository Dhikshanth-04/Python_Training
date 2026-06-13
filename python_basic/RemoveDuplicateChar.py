def removeDuplicate(str1):
    freq = {}
    res = ""
    for i in str1:
        freq[i] = freq.get(i,0)+1
    for i in freq:
        res+=i
    return res



str1 = input("Enter string : ")
res = removeDuplicate(str1)
print(res)