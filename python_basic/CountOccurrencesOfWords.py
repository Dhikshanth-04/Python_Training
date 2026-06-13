def countWords(str1):
    freq = {}
    index = 0
    for i in str1.split():
        freq[i] = freq.get(i,0)+1
    print(freq)


str1 = input("Enter the string : ")
countWords(str1)
