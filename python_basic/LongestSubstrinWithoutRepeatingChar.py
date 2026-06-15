def longestSubstringWithoutRepeatingChar(str1):
    left = 0
    seen = set()
    maxSum = 0
    for  right in range(len(str1)):
        while str1[right] in seen:
            seen.remove(str1[left])
            left+=1
        seen.add(str1[right])
        if right-left+1 > maxSum:
            maxSum = right-left+1
            best = left

    return str1[best:best+maxSum]

str1 = input("Enter string : ")
res = longestSubstringWithoutRepeatingChar(str1)
print(res)
