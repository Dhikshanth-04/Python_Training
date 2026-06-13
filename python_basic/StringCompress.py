def stringCompress(str1):
    res = ""
    freq = {}
    for i in str1:
        freq[i] = freq.get(i,0)+1
    for i in freq:
       res = res + i + str(freq[i])
    return res


str1 = input("Enter string : ")
res = stringCompress(str1)
print(res)