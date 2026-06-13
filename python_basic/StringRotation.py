def checkRotation(str1, str2):
    if len(str1)!=len(str2):
        return False
    return str2 in (str1+str1)


str1 = input("Enter the source string : ")
str2 = input("Enter the target string : ")
print(checkRotation(str1, str2))