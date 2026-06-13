def removeSpaces(str1):
    res = ""
    for i in str1:
        if i != ' ':
            res+=i
    return res


str1 = input("Enter string : ")
res = removeSpaces(str1)
print(res)