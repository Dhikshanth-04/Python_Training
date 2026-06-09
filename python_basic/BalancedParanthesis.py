def balancedParanthesis(s) ->bool:
   stack = []
   map = {')' : '(', ']' : '[', '}' : '{'}
   for i in s:
        if i in '([{':
            stack.append(i)
        elif i in ')}]':
            if not stack:
                return False
            top = stack.pop()
            if top!=map[i]:
                return False
   return True
    

s = input("Enter the string : ")
res = balancedParanthesis(s)
print(res)