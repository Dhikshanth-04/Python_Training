def frequencyCount(s):
    freq = {}
    for i in s:
        freq[i] = freq.get(i,0)+1
    return freq 

s = input("Enter string : ")
res = frequencyCount(s)
print(res)