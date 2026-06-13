def longestWord(str1):
    max = ""
    for i in str1.split():
        if len(max) < len(i):
            max = i
    return max


str1 = input("Enter string : ")
res = longestWord(str1)
print(res)