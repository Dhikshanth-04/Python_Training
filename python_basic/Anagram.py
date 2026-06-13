def checkAnagram(str1, str2):
    freq={}
    if len(str1) != len(str2):
        return False
    for i in str1:
        freq[i] = freq.get(i,0)+1
    for i in str2:
        freq[i] = freq.get(i,0)-1
    for i in freq:
        if freq[i]!=0:
            return False
    return True

str1 = input("Enter str1 : ")
str2 = input("Enter str2 : ")
print(checkAnagram(str1, str2))