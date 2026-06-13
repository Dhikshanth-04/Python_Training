def countupperLower(str1):
    upper = 0
    lower = 0
    for i in str1:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print("upper :", upper)
    print("Lower :", lower)


str1 = input("Enter string : ")
countupperLower(str1)
