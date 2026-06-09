def firstNonRepeatedChar(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0)+1
    for ch in s:
        if(freq[ch]==1):
            return ch

s = input("Enter the string : ")
res = firstNonRepeatedChar(s)
print("First non repeating char : ", res)
