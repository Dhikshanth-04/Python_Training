# yield - key word to denote the generator function
# next - retreives the next element from iterator
list = [1,2,3,4]
it = iter(list)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
#print(next(it))

#Lazy evaluation - instead of creating all values, create them only when its needed, generate later

def gen():
    yield 1
    yield 2
    yield 3
    yield 4

x = gen()
print(x)
print(next(x))
print(next(x))
print(next(x))

listComp = [i for i in range(10,1,-1) if i%2==0]
print(listComp)


    